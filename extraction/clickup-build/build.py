"""Build the chunks and tasks under the parent task in ClickUp, from manual/*/tasks.md.

Usage:
  python3 extraction/clickup-build/build.py --dry        # parse and report, no API calls
  python3 extraction/clickup-build/build.py --probe      # read-only: fields, tags, existing chunk subtasks
  python3 extraction/clickup-build/build.py --run        # create chunks, tasks, tags, then dependencies

Resumable: every created ID is saved to ids.json at once; a rerun skips what exists.
Type and phase are tags (type: decision/action/deliverable; phase: one of four).
Nothing is deleted or modified beyond what this script created.
"""
import re, glob, os, sys, json, time
sys.path.insert(0, '/Users/brandonacuna/Desktop/scaling-people:/extraction/s13')
B = '/Users/brandonacuna/Desktop/scaling-people:'
HERE = B + '/extraction/clickup-build/'
PARENT = '86akh1hdg'
LIST = '901323485125'
REPO = 'https://github.com/brandonjacuna/son-operational-buildout/blob/main/'
IDS = HERE + 'ids.json'
PHASES = {'before the first hire': 'phase: before first hire', 'hiring and training': 'phase: hiring and training',
          'before opening': 'phase: before opening', 'after opening': 'phase: after opening'}
TYPES = {'Decision': 'type: decision', 'Action': 'type: action', 'Deliverable': 'type: deliverable'}


def key(d):
    return [int(x) for x in os.path.basename(d.rstrip('/')).split('-')[0].split('.')]


def parse():
    chunks = []
    for d in sorted(glob.glob(B + '/manual/*/'), key=key):
        folder = os.path.basename(d.rstrip('/'))
        s = open(d + 'tasks.md').read()
        head = s.splitlines()[0].lstrip('# ').strip()
        sec = folder.split('-')[0]
        title = head.split(':')[0].strip()
        if not title.startswith(sec):
            title = f'{sec} {title}'
        tasks = []
        for num, ttl, body in re.findall(r'^### (\d+(?:\.\d+)+) (.+?)\n(.*?)(?=^### |^## |\Z)', s, re.M | re.S):
            f = lambda k: (re.search(rf'^- {k}:\s*(.+)$', body, re.M) or [None, ''])[1].strip()
            typ = f('Type'); ph = f('Phase').lower()
            phase = next((v for k, v in PHASES.items() if ph.startswith(k)), None)
            deps = sorted(set(re.findall(r'(?<![\d.])(\d\.\d{1,2}\.\d{1,2}|0\.\d{1,2})(?![\d])', f('Depends on'))))
            lines = [l for l in body.strip().splitlines() if l.startswith('- ')]
            desc = '\n'.join(lines) + f'\n\nManual: [{folder}]({REPO}manual/{folder}/) · session brief in `session.md` · record decisions in `decisions.md`.'
            tasks.append(dict(num=num, name=f'{num} {ttl.strip()}', type=typ, phase=phase, deps=deps, desc=desc))
        chunks.append(dict(sec=sec, name=title, folder=folder, tasks=tasks,
                           desc=f'Chunk {sec} of the Sŏn operational systems build out, in the book\'s order.\n\nManual: [{folder}]({REPO}manual/{folder}/): book.md, considerations.md, tasks.md, session.md, decisions.md.'))
    return chunks


def load():
    return json.load(open(IDS)) if os.path.exists(IDS) else {}


def save(ids):
    json.dump(ids, open(IDS, 'w'), indent=1, sort_keys=True)


def main():
    chunks = parse()
    all_tasks = {t['num']: t for c in chunks for t in c['tasks']}
    bad = [t['num'] for t in all_tasks.values() if t['type'] not in TYPES or not t['phase']]
    edges = [(t['num'], d) for t in all_tasks.values() for d in t['deps'] if d in all_tasks]
    missing = sorted({d for t in all_tasks.values() for d in t['deps'] if d not in all_tasks})
    print(f'{len(chunks)} chunks, {len(all_tasks)} tasks, {len(edges)} dependencies; bad type/phase: {bad}; deps not found: {missing}')
    if '--dry' in sys.argv:
        c = chunks[5]; t = c['tasks'][0]
        print('\nSample chunk:', c['name']); print('Sample task:', t['name'], TYPES.get(t['type']), t['phase'], t['deps']); print(t['desc'][:900])
        return
    import cu
    if '--probe' in sys.argv:
        f = cu.req('GET', f'list/{LIST}/field')
        for x in f.get('fields', []):
            print('field', x['name'], x['type'])
        lst = cu.req('GET', f'list/{LIST}')
        print('statuses', [s['status'] for s in lst.get('statuses', [])])
        tags = cu.req('GET', f"space/{lst['space']['id']}/tag")
        print('tags', [x['name'] for x in tags.get('tags', [])])
        p = cu.req('GET', f'task/{PARENT}', params='?include_subtasks=true')
        subs = p.get('subtasks', [])
        names = {c['name'] for c in chunks}
        print('parent subtasks', len(subs), 'matching chunk names', [s['name'] for s in subs if s['name'] in names])
        return
    if '--run' not in sys.argv:
        sys.exit('pass --dry, --probe, or --run')
    if bad:
        sys.exit('fix type/phase first')
    ids = load()
    lst = cu.req('GET', f'list/{LIST}')
    space = lst['space']['id']
    have = {x['name'] for x in cu.req('GET', f'space/{space}/tag').get('tags', [])}
    for tg in list(TYPES.values()) + list(PHASES.values()):
        if tg not in have:
            cu.req('POST', f'space/{space}/tag', {'tag': {'name': tg}})
    existing = {s['name']: s['id'] for s in cu.req('GET', f'task/{PARENT}', params='?include_subtasks=true').get('subtasks', [])}
    for c in chunks:
        ck = 'chunk:' + c['sec']
        if ck not in ids:
            if c['name'] in existing:
                ids[ck] = existing[c['name']]
            else:
                r = cu.req('POST', f'list/{LIST}/task', {'name': c['name'], 'parent': PARENT, 'markdown_description': c['desc']})
                ids[ck] = r['id']
            save(ids)
        for t in c['tasks']:
            if t['num'] in ids:
                continue
            r = cu.req('POST', f'list/{LIST}/task', {'name': t['name'], 'parent': ids[ck], 'markdown_description': t['desc'],
                                                    'tags': [TYPES[t['type']], t['phase']]})
            ids[t['num']] = r['id']
            save(ids)
        print('built', c['name'], len(c['tasks']))
    done = set(ids.get('_deps', []))
    for a, b in edges:
        k = f'{a}<{b}'
        if k in done:
            continue
        for attempt in range(6):
            try:
                cu.req('POST', f'task/{ids[a]}/dependency', {'depends_on': ids[b]})
                break
            except RuntimeError as e:
                if 'already' in str(e).lower() or 'exist' in str(e).lower():
                    break
                raise
            except Exception:
                time.sleep(20)
        else:
            raise RuntimeError(f'gave up on {k}')
        done.add(k)
        if len(done) % 50 == 0:
            ids['_deps'] = sorted(done); save(ids)
    ids['_deps'] = sorted(done); save(ids)
    print('dependencies', len(done))


if __name__ == '__main__':
    main()
