"""Renumber tasks in each chunk's tasks.md in document order and rewrite every reference.

New tasks may carry placeholder numbers like 3.3.X1, 3.3.X2 (letter X plus digits).
Usage: python3 extraction/build/renumber.py [--dry]
Rewrites references in manual/**/*.md and kits/**/*.md. Reports references to numbers that no longer exist.
"""
import re, glob, os, sys
B = '/Users/brandonacuna/Desktop/scaling-people:'
dry = '--dry' in sys.argv
HEAD = re.compile(r'^### (\d+(?:\.\d+)*\.(?:\d+|X\d+)) ', re.M)
maps = {}
for d in glob.glob(B + '/manual/*/'):
    chunk = os.path.basename(d.rstrip('/')).split('-')[0]
    s = open(d + 'tasks.md').read()
    nums = HEAD.findall(s)
    for i, old in enumerate(nums, 1):
        new = f'{chunk}.{i}'
        if old != new:
            maps[old] = new
if not maps:
    print('nothing to renumber')
files = glob.glob(B + '/manual/**/*.md', recursive=True) + glob.glob(B + '/kits/**/*.md', recursive=True)
# pre-check: every reference must point at a current heading, or renumbering would silently repoint it
current = set()
for d in glob.glob(B + '/manual/*/'):
    current |= set(HEAD.findall(open(d + 'tasks.md').read()))
cprefix = {x.rsplit('.', 1)[0] for x in current}
stale = {}
for f in files:
    for r in set(re.findall(r'(?<![\d.])(\d\.\d{1,2}\.(?:X\d+|\d{1,2}))(?![\d])', open(f).read())):
        if r not in current and r.rsplit('.', 1)[0] in cprefix:
            stale.setdefault(r, []).append(os.path.relpath(f, B))
if stale and '--force' not in sys.argv:
    for r, fs in sorted(stale.items()):
        print('stale reference', r, fs[:4])
    sys.exit('Stale references found: repoint them before renumbering (or --force).')
tok = re.compile(r'(?<![\d.])(\d\.\d{1,2}\.(?:X\d+|\d{1,2}))(?![\d])')
changed = 0
for f in files:
    s = open(f).read()
    t = tok.sub(lambda m: '\0' + maps[m.group(1)] + '\0' if m.group(1) in maps else m.group(0), s).replace('\0', '')
    if t != s:
        changed += 1
        if not dry:
            open(f, 'w').write(t)
print(f'{len(maps)} numbers remapped, {changed} files {"would change" if dry else "changed"}')
# report dangling references
defined = set()
for d in glob.glob(B + '/manual/*/'):
    src = open(d + 'tasks.md').read()
    if not dry:
        defined |= set(re.findall(r'^### (\d+(?:\.\d+)+) ', src, re.M))
    else:
        defined |= {maps.get(n, n) for n in HEAD.findall(src)}
prefixes = {x.rsplit('.', 1)[0] for x in defined}
dang = {}
for f in files:
    for r in set(re.findall(r'(?<![\d.])(\d\.\d{1,2}\.\d{1,2})(?![\d])', open(f).read())):
        if r not in defined and r.rsplit('.', 1)[0] in prefixes:
            dang.setdefault(r, []).append(os.path.relpath(f, B))
for r, fs in sorted(dang.items()):
    print('dangling', r, fs[:4])
