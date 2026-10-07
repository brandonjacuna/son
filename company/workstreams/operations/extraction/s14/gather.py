import sys, json
sys.path.insert(0,'../s13')
from cu import req, page_get
# ledger
p=page_get('2ky45bmy-17233','2ky45bmy-30353')
open('tracker-before.md','w').write(p.get('content',''))
# session task
t=req('GET','task/86ajgmjk1',params='?include_markdown_description=true')
open('session-task.json','w').write(json.dumps(t,indent=1))
links=[l['task_id'] if l['task_id']!='86ajgmjk1' else l['link_id'] for l in t.get('linked_tasks',[])]
out=['# S14 carryovers (tasks linked to session task 86ajgmjk1)\n',f'Retrieved 2026-09-24 over REST. {len(links)} linked tasks.\n']
summ=[]
for lid in links:
    lt=req('GET',f'task/{lid}',params='?include_markdown_description=true')
    cm=req('GET',f'task/{lid}/comment').get('comments',[])
    summ.append(f"| {lid} | {lt['name']} | {lt['list']['name']} | {lt['status']['status']} | {len(cm)} comments |")
    out.append(f"\n---\n\n## {lid}: {lt['name']}\n\nList: {lt['list']['name']} ({lt['list']['id']}). Status: {lt['status']['status']}. Priority: {(lt.get('priority') or {}).get('priority')}.\n\n### Description\n\n{lt.get('markdown_description') or lt.get('description')}\n")
    for c in reversed(cm):
        out.append(f"\n### Comment ({c['user']['username']}, {c['date']})\n\n{c['comment_text']}\n")
open('carryovers.md','w').write(out[0]+out[1]+'\n| id | name | list | status | comments |\n|---|---|---|---|---|\n'+'\n'.join(summ)+'\n'+''.join(out[2:]))
# punch list subtasks
par=req('GET','task/86akh1hdg',params='?include_subtasks=true')
subs=par.get('subtasks',[])
open('punch-list-existing.md','w').write(f'Total: {len(subs)}\n'+'\n'.join(f"{s['id']} | {s['status']['status']} | {s['name']}" for s in subs)+'\n')
print(len(p.get('content','')), len(links), len(subs))
print('\n'.join(summ))
print((t.get('markdown_description') or t.get('description')))
