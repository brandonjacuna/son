import sys,json,os,time; sys.path.insert(0,'../../extraction/s13')
from cu import req
def r(*a,**k):
    for i in range(6):
        try: return req(*a,**k)
        except Exception as e:
            if 'timed out' in str(e) or 'URLError' in type(e).__name__ or '5' == str(e)[:1]: time.sleep(5*(i+1)); continue
            raise
    raise RuntimeError('gave up')
os.makedirs('tasks',exist_ok=True)
def dump(tid):
    f=f'tasks/{tid}.json'
    if os.path.exists(f): return json.load(open(f))
    t=r('GET',f'task/{tid}',params='?include_markdown_description=true&include_subtasks=true')
    t['_comments']=r('GET',f'task/{tid}/comment').get('comments',[])
    json.dump(t,open(f,'w'),indent=1); return t
for parent,name in [('86akh1hdg','buildout-subtasks'),('86ajgmh9a','session-tasks')]:
    p=dump(parent); subs=[dump(s['id']) for s in p.get('subtasks',[])]
    # third level if any
    deep=[dump(ss['id']) for s in subs for ss in s.get('subtasks',[])]
    json.dump({'parent':p,'subtasks':subs,'deeper':deep},open(f'{name}.json','w'),indent=1); print(name,len(subs),len(deep))
