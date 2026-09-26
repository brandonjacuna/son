import sys, json
sys.path.insert(0,'../s13')
from cu import req, page_get
p=page_get('2ky45bmy-17233','2ky45bmy-30353')
open('tracker-before.md','w').write(p.get('content',''))
t=req('GET','task/86ajgmjpw',params='?include_markdown_description=true')
json.dump(t,open('session-task.json','w'),indent=1)
print(t['name'], t['status']['status'])
links=[l for l in t.get('linked_tasks',[])]
out=[]
for l in links:
    oid = l['link_id'] if l['task_id']=='86ajgmjpw' else l['task_id']
    lt=req('GET',f'task/{oid}',params='?include_markdown_description=true')
    c=req('GET',f'task/{oid}/comment')
    out.append({'id':oid,'name':lt['name'],'status':lt['status']['status'],'list':lt['list']['name'],'desc':lt.get('markdown_description') or lt.get('description'),'comments':[x['comment_text'] for x in c.get('comments',[])]})
json.dump(out,open('carryovers.json','w'),indent=1)
for o in out: print(o['id'],o['status'],o['list'],'|',o['name'])
