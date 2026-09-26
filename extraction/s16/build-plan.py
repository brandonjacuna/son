import re, json
src=open('../../output/s16/work-items-and-carryovers.md',encoding='utf-8').read()
PROV="Filed by Session 16 of the Scaling People translation program. Session task `86ajgmjz6`. Reasoning lives on the S16 page of the Sŏn Operating System doc `2ky45bmy-17253`."
A=src[src.index('## A.'):src.index('## B.')]
B=src[src.index('## B.'):src.index('## C.')]
C=src[src.index('## C.'):]
items=[]; typ=None
for para in A.split('\n\n'):
    para=para.strip()
    m=re.match(r'### (\w[\w ]*?)(\s*\(|$)',para)
    if m: typ=m.group(1).strip(); continue
    m=re.match(r'\*\*(A\d+)\. (.+?)\*\* (.+)$',para,re.S)
    if not m: continue
    k,title,desc=m.groups()
    title=title.rstrip('.')
    if typ=='Instrument' and '86ajgn2z5' not in title: title+=' (gated on `86ajgn2z5`)'
    pr=re.search(r'(Urgent|High|Normal)\.$',desc.strip())
    items.append(dict(k=k,name=f'{typ}: {title}',priority=pr.group(1).lower() if pr else None,desc=desc.strip()+'\n\n'+PROV))
SES={'S16':'86ajgmjz6','S17':'86ajgmk27'}
for para in B.split('\n\n'):
    para=para.strip()
    m=re.match(r'\*\*(B\d+)\. (.+?)\*\* → (S\d+) \(`(\w+)`\)\. (Urgent|High|Normal)\. (.+)$',para,re.S)
    if not m: 
        if para.startswith('**B'): print('BFAIL',para[:120])
        continue
    k,title,s,tid,pr,desc=m.groups()
    assert SES[s]==tid
    items.append(dict(k=k,name=title.rstrip('.'),priority=pr.lower(),target=tid,session=s,
        desc=f'**Routed to: {s} (`{tid}`)**\n\n'+desc.strip()+'\n\n'+PROV))
comments=[]
for para in C.split('\n\n'):
    para=para.strip()
    if not para.startswith('**`'): continue
    ci=para.index('Comment')
    head=para[:ci]; rest=para[ci:]
    ids=re.findall(r'\*\*`((?:86a|17t)\w+)`\*\*',head)
    m=re.search(r'Comment(?: for each)?: (.+)$',rest,re.S)
    if not m: print('CFAIL',para[:100]); continue
    t=m.group(1).strip()
    if t.startswith('"') and t.endswith('"'): t=t[1:-1]
    t=t.replace('`','')
    comments.append(dict(ids=ids,status=head.split(')',1)[-1].strip(' .'),text=t))
json.dump(dict(items=items,comments=comments),open('filing-plan.json','w'),ensure_ascii=False,indent=1)
print(len(items),'items;',sum(len(c['ids']) for c in comments),'comment targets in',len(comments),'entries')
for it in items: print(it['k'],it['priority'],it['desc'].count('Filed by Session'),it['name'][:110])
for c in comments: print(c['ids'],c['text'][:1].isupper(),len(c['text']))
