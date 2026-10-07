"""
build_scene.py  —  Batched-espresso café setup, parametric Blender build.

Run:  blender --background --python build_scene.py
      (or paste into Blender's Scripting workspace and Run Script)

UNITS: this script works in METRES and converts from the millimetre dimensions in
blender_component_schedule.csv. Blender's default unit scale is 1 m == 1 BU, so every
dimension below is written as mm * MM.

COORDINATE SYSTEM (matches fig_fill_station_layout.png):
    origin  = counter LEFT end / FRONT edge / FLOOR level
    +X      = right, along the counter run (0 .. 2000 mm)
    +Y      = back, toward the wall        (0 .. 650 mm)
    +Z      = up from the floor            (floor 0, counter top 900 mm)

The two parts that are geometrically load-bearing are build_coil() and
build_keg_assembly(). Everything else is a box or a cylinder and can be replaced with a
purchased asset without breaking the layout.

SCOPE: back-of-house FILL STATION only. One keg is filled at a time and held at <=4 degC
until it is carried to front-of-house. There is NO tap and NO dispensing hardware in this
scene - that lives in the front area and is not designed yet.
"""
import bpy, bmesh, math
from mathutils import Vector

MM = 0.001

# ----------------------------------------------------------------------------- helpers
def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for c in (bpy.data.meshes, bpy.data.materials, bpy.data.curves):
        for b in list(c):
            if b.users == 0:
                c.remove(b)

def mat(name, base, metallic=0.0, rough=0.5, alpha=1.0, ior=1.45):
    """Principled BSDF. Socket names are Blender 4.x; see note at the bottom for 3.x."""
    m = bpy.data.materials.get(name)
    if m:
        return m
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    p = m.node_tree.nodes["Principled BSDF"]
    p.inputs["Base Color"].default_value = (*base, 1.0)
    p.inputs["Metallic"].default_value = metallic
    p.inputs["Roughness"].default_value = rough
    if alpha < 1.0:
        p.inputs["Alpha"].default_value = alpha
        p.inputs["IOR"].default_value = ior
        m.blend_method = "BLEND"
    return m

def box(name, size_mm, loc_mm, material=None, pivot="corner"):
    """size_mm=(L,W,H) along X,Y,Z. pivot='corner' puts loc at the min corner."""
    L, W, H = (s * MM for s in size_mm)
    bpy.ops.mesh.primitive_cube_add(size=1)
    ob = bpy.context.object
    ob.name = name
    ob.scale = (L, W, H)
    x, y, z = (v * MM for v in loc_mm)
    ob.location = (x + L/2, y + W/2, z + H/2) if pivot == "corner" else (x, y, z)
    if material:
        ob.data.materials.append(material)
    return ob

def cyl(name, dia_mm, h_mm, loc_mm, material=None, verts=64, axis="Z"):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=dia_mm*MM/2, depth=h_mm*MM)
    ob = bpy.context.object
    ob.name = name
    x, y, z = (v * MM for v in loc_mm)
    ob.location = (x, y, z + h_mm*MM/2)
    if axis == "Y":
        ob.rotation_euler = (math.pi/2, 0, 0)
    if material:
        ob.data.materials.append(material)
    return ob

# ----------------------------------------------------------------------------- the coil
# THE one part with no off-the-shelf equivalent. Values are exact, from the thermal design.
COIL = dict(
    bore_mm      = 3.0,     # internal — sets holdup volume, do not change casually
    wall_mm      = 0.7,
    od_mm        = 4.4,     # 3.0 + 2*0.7
    coil_dia_mm  = 80.0,    # helix diameter, centreline of the tube
    turns        = 9,
    pitch_mm     = 15.5,    # rise per turn; leaves an 11.1 mm gap for glycol to flow between turns
)
# derived, for reference: developed length 2266 mm, rise 139.5 mm, internal volume 16.0 mL

def build_coil(name="chiller_coil", loc_mm=(0, 0, 0), material=None, res=24):
    """Helical tube. res = points per turn; 24 is smooth at render scale, 48 for close-ups.

    Built as a poly curve + round bevel, which gives a true tube wall thickness of zero
    (a surface, not a solid). That is correct for render; if you need a solid for a
    cutaway, add a Solidify modifier of COIL['wall_mm'].
    """
    r     = COIL["coil_dia_mm"] * MM / 2
    pitch = COIL["pitch_mm"] * MM
    n     = COIL["turns"] * res

    cu = bpy.data.curves.new(name + "_curve", type="CURVE")
    cu.dimensions = "3D"
    cu.resolution_u = 4
    sp = cu.splines.new("POLY")
    sp.points.add(n)                       # add() is on top of the 1 existing point
    for i in range(n + 1):
        t = 2*math.pi * COIL["turns"] * i / n
        sp.points[i].co = (r*math.cos(t), r*math.sin(t), pitch * t/(2*math.pi), 1.0)

    # round profile = the tube
    cu.bevel_mode   = "ROUND"
    cu.bevel_depth  = COIL["od_mm"] * MM / 2
    cu.bevel_resolution = 6
    cu.use_fill_caps = True

    ob = bpy.data.objects.new(name, cu)
    bpy.context.collection.objects.link(ob)
    ob.location = tuple(v * MM for v in loc_mm)
    if material:
        ob.data.materials.append(material)
    return ob

def coil_endpoints_mm():
    """Where the plumbing must meet the coil. Inlet is at the BOTTOM — see the flow note."""
    r = COIL["coil_dia_mm"] / 2
    rise = COIL["pitch_mm"] * COIL["turns"]
    t_end = 2*math.pi*COIL["turns"]
    return dict(inlet=(r, 0.0, 0.0),
                outlet=(r*math.cos(t_end), r*math.sin(t_end), rise))

# ------------------------------------------------------------------- the nitro blanket
KEG = dict(body_dia_mm=229.0, body_h_mm=279.0, wall_mm=1.2,
           fill_L=4.0, total_L=6.0,
           post_dia_mm=19.0, post_h_mm=28.0, post_pitch_mm=76.0,
           dip_od_mm=7.9, dip_clearance_mm=5.0)

def build_keg_assembly(name="keg", loc_mm=(0, 0, 0), cutaway=False):
    """Mini corny keg + gas blanket internals.

    cutaway=True also creates the liquid body and the gas headspace as separate visible
    volumes, which is what you want for the hero shot of the blanket. The headspace is
    the POINT of this assembly — it is the thing the whole system exists to control.
    """
    steel  = mat("steel_304_brushed", (0.62, 0.63, 0.64), metallic=1.0, rough=0.35)
    coffee = mat("coffee_dark",       (0.07, 0.035, 0.018), rough=0.15, alpha=0.92, ior=1.36)
    gas    = mat("blanket_gas",       (0.55, 0.78, 0.88), rough=1.0, alpha=0.10)
    grey_p = mat("plastic_grey",      (0.52, 0.54, 0.56), rough=0.55)
    black_p= mat("plastic_black",     (0.04, 0.04, 0.045), rough=0.50)
    glass  = mat("glass_clear",       (0.95, 0.97, 0.98), rough=0.02, alpha=0.08, ior=1.52)

    x, y, z = loc_mm
    out = {}
    out["body"] = cyl(f"{name}_body", KEG["body_dia_mm"], KEG["body_h_mm"], (x, y, z), steel)

    # --- liquid level and headspace -----------------------------------------------
    area_mm2  = math.pi * (KEG["body_dia_mm"]/2)**2
    liquid_h  = KEG["fill_L"] * 1e6 / area_mm2            # mm;  4 L in a 229 mm bore
    head_h    = KEG["body_h_mm"] - liquid_h
    out["liquid_h_mm"], out["headspace_h_mm"] = liquid_h, head_h
    if cutaway:
        d_in = KEG["body_dia_mm"] - 2*KEG["wall_mm"]
        out["liquid"]    = cyl(f"{name}_liquid", d_in, liquid_h, (x, y, z), coffee)
        out["headspace"] = cyl(f"{name}_headspace", d_in, head_h, (x, y, z + liquid_h), gas)

    # --- the two ball-lock posts, on the lid --------------------------------------
    zp = z + KEG["body_h_mm"]
    for tag, dx, dmat in (("gas_in", -KEG["post_pitch_mm"]/2, grey_p),
                          ("liquid_out", +KEG["post_pitch_mm"]/2, black_p)):
        out[f"post_{tag}"] = cyl(f"{name}_post_{tag}", KEG["post_dia_mm"],
                                 KEG["post_h_mm"], (x + dx, y, zp), steel)
        out[f"qd_{tag}"]   = cyl(f"{name}_qd_{tag}", 26.0, 52.0,
                                 (x + dx, y, zp + KEG["post_h_mm"]), dmat)

    # --- internals: the detail that makes the blanket work -------------------------
    # Gas tube is SHORT: it must terminate in the headspace, never below liquid level,
    # or incoming gas sparges the coffee and strips its CO2.
    out["gas_tube"] = cyl(f"{name}_gas_tube", KEG["dip_od_mm"], 25.0,
                          (x - KEG["post_pitch_mm"]/2, y, zp - 25.0), steel)
    # Liquid dip tube runs to just off the floor and is the FILL path, so coffee enters
    # below the surface and never falls through the gas. (It is also the eventual draw path
    # once the keg reaches front-of-house, but no draw hardware is modelled here.)
    dip_h = KEG["body_h_mm"] - KEG["dip_clearance_mm"]
    out["dip_tube"] = cyl(f"{name}_dip_tube", KEG["dip_od_mm"], dip_h,
                          (x + KEG["post_pitch_mm"]/2, y, z + KEG["dip_clearance_mm"]), steel)

    # --- sight glass for the oxygen sensor spot ------------------------------------
    # Optical O2 spots are read THROUGH a transparent wall. A stainless keg is opaque, so
    # the instrumented keg needs a window. Boss at mid-liquid height, facing -Y (front).
    sg = cyl(f"{name}_sight_glass", 25.0, 6.0,
             (x, y - KEG["body_dia_mm"]/2, z + liquid_h/2), glass, axis="Y")
    out["sight_glass"] = sg
    spot = cyl(f"{name}_o2_spot", 5.0, 0.5,
               (x, y - KEG["body_dia_mm"]/2 + 3.0, z + liquid_h/2),
               mat("sensor_spot", (0.85, 0.42, 0.55), rough=0.6), axis="Y")
    out["o2_spot"] = spot
    return out

# ----------------------------------------------------------------------------- the room
def build_scene(cutaway_keg=True):
    """Back-of-house fill station. One keg, refrigerated, no dispensing."""
    clear_scene()
    stone   = mat("stone_honed",  (0.78, 0.76, 0.72), rough=0.45)
    carcass = mat("laminate_dark",(0.13, 0.13, 0.14), rough=0.55)
    tile    = mat("tile_gloss",   (0.93, 0.94, 0.94), rough=0.10)
    steel   = mat("steel_brushed",(0.60, 0.61, 0.62), metallic=1.0, rough=0.30)
    poly    = mat("steel_316L_bright",(0.70, 0.71, 0.72), metallic=1.0, rough=0.18)
    foam    = mat("foam_closed_cell",(0.16, 0.17, 0.18), rough=0.85)
    painted = mat("steel_painted_grey",(0.42, 0.44, 0.47), rough=0.40)
    glass   = mat("glass_clear",  (0.95, 0.97, 0.98), rough=0.02, alpha=0.08, ior=1.52)

    box("counter_top",     (2000, 650, 40),  (0, 0, 860), stone)
    box("counter_carcass", (2000, 620, 860), (0, 30, 0),  carcass)
    box("back_wall",       (2000, 20, 1400), (0, 650, 0), tile)

    # --- on the counter ---
    box("espresso_machine",(800, 560, 520),  (380, 60, 900),  steel)
    box("grinder",         (230, 400, 620),  (80, 150, 900),  steel)
    box("bath_insulation", (210, 180, 250),  (1270, 400, 900), foam)
    box("bath_vessel",     (160, 130, 200),  (1295, 425, 925), steel)
    for i, dx in enumerate((1330, 1410)):
        build_coil(f"chiller_coil_{i+1}", loc_mm=(dx, 490, 945), material=poly)

    # --- below the counter: the refrigerated fill well ---
    box("fill_well",   (400, 500, 820), (1250, 40, 20),  steel)
    box("bench_scale", (300, 300, 90),  (1300, 140, 80), steel)
    box("glycol_power_pack", (400, 400, 500), (400, 60, 20), painted)
    cyl("gas_cylinder", 133.0, 457.0, (1816, 486, 20), painted)

    # the one keg, sitting on the scale inside the well
    keg = build_keg_assembly("keg", loc_mm=(1449, 290, 170), cutaway=cutaway_keg)

    # --- purge / vent manifold: the custom part of the blanket system ---
    box("purge_manifold", (180, 90, 110), (1660, 250, 560), mat("steel_316",(0.68,0.69,0.70),
                                                                metallic=1.0, rough=0.25))
    cyl("vent_bubbler", 60.0, 180.0, (1700, 150, 360), glass)
    return keg

# ----------------------------------------------------------------------------- cameras
def add_cameras():
    """Two things are asked for: the whole station, and the gas blanket in high detail."""
    shots = [
        # name,              location_mm,               look-at target_mm,    lens_mm
        ("CAM_station_wide", (-800, -1500, 1600),       (1000, 325, 780),     35),
        ("CAM_station_34",   (2600, -1300, 1450),       (1300, 325, 900),     50),
        ("CAM_blanket_hero", (1449-240, 290-430, 480),  (1449, 290, 320),     85),
        ("CAM_blanket_top",  (1449+120, 290-180, 760),  (1449, 290, 450),     60),
        ("CAM_coil_detail",  (1370+170, 490-230, 1080), (1370, 490, 1020),   100),
    ]
    for name, loc, tgt, lens in shots:
        bpy.ops.object.camera_add(location=tuple(v*MM for v in loc))
        c = bpy.context.object
        c.name, c.data.lens = name, lens
        c.data.dof.use_dof = True
        c.data.dof.focus_distance = (Vector([v*MM for v in loc])
                                     - Vector([v*MM for v in tgt])).length
        c.data.dof.aperture_fstop = 4.0 if ("blanket" in name or "detail" in name) else 8.0
        e = bpy.data.objects.new(name + "_target", None)
        bpy.context.collection.objects.link(e)
        e.location = tuple(v*MM for v in tgt)
        trk = c.constraints.new("TRACK_TO")
        trk.target, trk.track_axis, trk.up_axis = e, "TRACK_NEGATIVE_Z", "UP_Y"

def add_lighting():
    """Cafe-plausible: broad key from the shopfront, cool fill, warm pendant."""
    bpy.ops.object.light_add(type="AREA", location=(-1.0, -2.2, 2.3))
    k = bpy.context.object; k.name = "KEY_shopfront"
    k.data.energy, k.data.size, k.data.color = 400, 2.5, (1.0, 0.96, 0.90)
    k.rotation_euler = (math.radians(62), 0, math.radians(-38))
    bpy.ops.object.light_add(type="AREA", location=(2.6, -1.4, 2.0))
    f = bpy.context.object; f.name = "FILL_cool"
    f.data.energy, f.data.size, f.data.color = 110, 1.8, (0.88, 0.93, 1.0)
    f.rotation_euler = (math.radians(66), 0, math.radians(48))
    bpy.ops.object.light_add(type="POINT", location=(1.1, 0.3, 1.9))
    p = bpy.context.object; p.name = "PENDANT_warm"
    p.data.energy, p.data.color, p.data.shadow_soft_size = 60, (1.0, 0.82, 0.62), 0.09

def setup_render(samples=256):
    s = bpy.context.scene
    s.render.engine = "CYCLES"
    s.cycles.samples, s.cycles.use_denoising = samples, True
    s.render.resolution_x, s.render.resolution_y = 2400, 1600
    s.view_settings.view_transform = "AgX"   # 'Filmic' on Blender < 4.0

if __name__ == "__main__":
    keg = build_scene(cutaway_keg=True)
    add_cameras(); add_lighting(); setup_render()
    print(f"[ok] liquid depth {keg['liquid_h_mm']:.1f} mm, "
          f"headspace {keg['headspace_h_mm']:.1f} mm")
    print(f"[ok] coil endpoints (mm, local to coil origin): {coil_endpoints_mm()}")

# -----------------------------------------------------------------------------
# BLENDER VERSION NOTE
# Written against Blender 4.x. On 3.6 and earlier:
#   - Principled BSDF: drop the "IOR" line (socket differs).
#   - view_transform "AgX" does not exist; use "Filmic".
#   - curve .bevel_mode exists from 2.9; on older builds set .bevel_depth only.
# Verify in the actual target version before trusting the material look.
