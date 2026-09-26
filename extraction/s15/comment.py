import sys,json,os; sys.path.insert(0,'../s13')
from cu import req
PROV="Filed by Session 15 of the Scaling People translation program. Session task 86ajgmjpw. Reasoning lives on the S15 page of the Sŏn Operating System doc 2ky45bmy-17253."
plan=json.load(open('filing-plan.json'))
done={l.split('\t')[0] for l in open('comments-log.tsv')} if os.path.exists('comments-log.tsv') else set()
log=open('comments-log.tsv','a')
for c in plan['comments']:
    for tid in c['ids']:
        if tid in done: continue
        txt=c['text']+'\n\n'+PROV
        r=req('POST',f'task/{tid}/comment',{'comment_text':txt,'notify_all':False})
        log.write(f"{tid}\t{r.get('id')}\n"); log.flush(); print(tid,r.get('id'))
