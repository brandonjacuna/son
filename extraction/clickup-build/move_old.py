"""Move the 400 old build-out subtasks under the holding task. Resumable via holding.json."""
import sys, json; sys.path.insert(0, '/Users/brandonacuna/Desktop/scaling-people:/extraction/s13'); import cu
B = '/Users/brandonacuna/Desktop/scaling-people:/'
H = B + 'extraction/clickup-build/holding.json'
st = json.load(open(H)); hid = st['holding']; moved = set(st['moved'])
old = [s['id'] for s in json.load(open(B + 'archive/clickup-export-2026-09-26/buildout-subtasks.json'))['subtasks']]
for i, t in enumerate(old):
    if t in moved: continue
    cu.req('PUT', f'task/{t}', {'parent': hid}); moved.add(t)
    if len(moved) % 25 == 0: st['moved'] = sorted(moved); json.dump(st, open(H, 'w'))
st['moved'] = sorted(moved); json.dump(st, open(H, 'w'))
print('moved', len(moved), 'of', len(old))
