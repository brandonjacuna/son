import sys,json,re,os; sys.path.insert(0,'../s13')
from cu import req
P={1:'urgent',2:'high',3:'normal'}
plan={i['k']:i for i in json.load(open('filing-plan.json'))['items']}
os.makedirs('verify',exist_ok=True)
def n(t): return re.sub(r'\s+',' ',re.sub(r'[\\*`]','',t)).strip()
bad=0
for l in open('filed.tsv'):
    k,tid,name=l.rstrip('\n').split('\t'); it=plan[k]
    t=req('GET',f'task/{tid}',params='?include_markdown_description=true'); json.dump(t,open(f'verify/{k}.json','w'))
    probs=[]
    if t['name']!=it['name']: probs.append('name')
    if P.get(int((t.get('priority') or {}).get('id',0)))!=it['priority']: probs.append('prio')
    if k.startswith('A') and t.get('parent')!='86akh1hdg': probs.append('parent')
    if k.startswith('B') and it['target'] not in json.dumps(t.get('linked_tasks',[])): probs.append('link')
    if n(t.get('markdown_description') or '')!=n(it['desc']): probs.append('desc')
    if (t.get('markdown_description') or '').count('Filed by Session')!=1: probs.append('prov')
    if probs: bad+=1; print(k,probs)
print('bad',bad)
