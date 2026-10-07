import sys,json,os; sys.path.insert(0,'../../extraction/s13')
from cu import req,WS
def pages(doc):
    r=req('GET',f'workspaces/{WS}/docs/{doc}/pageListing',v='v3')
    out=[]
    def walk(ps,depth=0):
        for p in ps: out.append((p['id'],p.get('name',''),depth)); walk(p.get('pages',[]),depth+1)
    walk(r if isinstance(r,list) else r.get('pages',[])); return out
for doc,name in [('2ky45bmy-17253','operating-system-doc'),('2ky45bmy-17233','tracker-doc')]:
    os.makedirs(name,exist_ok=True); idx=[]
    for i,(pid,title,dep) in enumerate(pages(doc),1):
        c=req('GET',f'workspaces/{WS}/docs/{doc}/pages/{pid}',v='v3',params='?content_format=text/md').get('content','')
        fn=f'{i:02}-{pid}.md'; open(f'{name}/{fn}','w',encoding='utf-8').write(f'# {title}\n\n'+c)
        idx.append(f'| {i} | {pid} | {title} | {len(c)} |')
    open(f'{name}/INDEX.md','w').write('| # | page | title | chars |\n|---|---|---|---|\n'+'\n'.join(idx)+'\n')
    print(name,len(idx))
def dump_task(tid):
    t=req('GET',f'task/{tid}',params='?include_markdown_description=true&include_subtasks=true')
    t['_comments']=req('GET',f'task/{tid}/comment').get('comments',[]); return t
def dump_list_tasks(list_id):
    out=[];page=0
    while True:
        r=req('GET',f'list/{list_id}/task',params=f'?page={page}&include_closed=true&subtasks=true&include_markdown_description=true')
        out+=r.get('tasks',[])
        if r.get('last_page',True) or not r.get('tasks'): break
        page+=1
    return out
# carryover register
cr=dump_list_tasks('901327884538')
for t in cr: t['_comments']=req('GET',f"task/{t['id']}/comment").get('comments',[])
json.dump(cr,open('carryover-register.json','w'),indent=1); print('carryovers',len(cr))
# punch list parent and subtasks, session parent and subtasks
for parent,name in [('86akh1hdg','buildout-subtasks'),('86ajgmh9a','session-tasks')]:
    p=dump_task(parent); subs=[dump_task(s['id']) for s in p.get('subtasks',[])]
    json.dump({'parent':p,'subtasks':subs},open(f'{name}.json','w'),indent=1); print(name,len(subs))
