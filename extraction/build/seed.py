"""Seed decisions.md and notes/inbox.md for every chunk folder whose tasks.md exists. Doesn't overwrite existing decisions.md."""
import re,os,glob,sys
for d in sorted(glob.glob('/Users/brandonacuna/Desktop/scaling-people:/manual/*/')):
    t=os.path.join(d,'tasks.md')
    if not os.path.exists(t): continue
    sec,title=os.path.basename(d.rstrip('/')).split('-',1)[0],None
    name=open(t,encoding='utf-8').readline().lstrip('# ').split(':')[0].strip()
    os.makedirs(d+'notes',exist_ok=True)
    inbox=d+'notes/inbox.md'
    if not os.path.exists(inbox): open(inbox,'w').write(f'# {sec} inbox: items raised elsewhere that belong to this chunk\n')
    dm=d+'decisions.md'
    if os.path.exists(dm): continue
    txt=open(t,encoding='utf-8').read()
    blocks=re.findall(r'^### (\S+) (.+?)\n(.*?)(?=^### |\Z)',txt,re.M|re.S)
    decs=[(n,ti) for n,ti,body in blocks if re.search(r'Type:\s*Decision',body)]
    out=[f'# {name}: decisions\n\nRecorded in Brandon\'s words, with his reasoning. Status is open, decided, pending agreement from ..., or parked.\n']
    for n,ti in decs: out.append(f'\n## {n} {ti}\n- Status: open\n- Decision:\n- Reasoning (his words):\n- Date:\n- Still needs:\n')
    open(dm,'w',encoding='utf-8').write(''.join(out)); print(dm,len(decs))
