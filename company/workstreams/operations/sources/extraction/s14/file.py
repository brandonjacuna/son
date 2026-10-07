import sys,json,os,time; sys.path.insert(0,'../s13')
from cu import req
P={'urgent':1,'high':2,'normal':3}
plan=json.load(open('filing-plan.json'))
done={l.split('\t')[0] for l in open('filed.tsv')} if os.path.exists('filed.tsv') else set()
out=open('filed.tsv','a')
for it in plan['items']:
    if it['k'] in done: continue
    body={'name':it['name'],'markdown_content':it['desc'],'priority':P[it['priority']]}
    lst='901323485125' if it['k'].startswith('A') else '901327884538'
    if it['k'].startswith('A'): body['parent']='86akh1hdg'
    try: r=req('POST',f'list/{lst}/task',body)
    except RuntimeError as e:
        print('ERR',it['k'],str(e)[:80]); time.sleep(5)
        q=req('GET',f'list/{lst}/task',params='?subtasks=true&include_closed=true&order_by=created&reverse=false&page=0')['tasks']
        m=[t for t in q if t['name']==it['name']]
        if not m: raise
        r=m[0]
    if it['k'].startswith('B'): req('POST',f"task/{r['id']}/link/{it['target']}")
    out.write(f"{it['k']}\t{r['id']}\t{it['name']}\n"); out.flush(); print(it['k'],r['id'])
