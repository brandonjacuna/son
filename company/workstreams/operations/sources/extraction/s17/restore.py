import sys,re,time,difflib; sys.path.insert(0,'../s13')
from cu import page_append,page_get
D,P='2ky45bmy-17233','2ky45bmy-30353'
new=open('tracker-after.md',encoding='utf-8').read(); src=open('tracker-before.md',encoding='utf-8').read()
parts=re.split(r'(?=\n\n)|(?=\n\*   )',new); chunks=[];cur=''
for p in parts:
    if cur and len((cur+p).encode())>12000: chunks.append(cur); cur=p
    else: cur+=p
chunks.append(cur)
n=lambda t: re.sub(r'[\\*`_#>|]',' ',t).split()
for i,c in enumerate(chunks[1:],2):
    target=n(''.join(chunks[:i]))
    for attempt in range(4):
        try: page_append(D,P,c); break
        except Exception as e:
            print('chunk',i,'error',str(e)[:120]); time.sleep(5)
            if n(page_get(D,P)['content'])==target: print('chunk',i,'landed despite error'); break
    live=n(page_get(D,P)['content'])
    assert live==target, f'mismatch after chunk {i}'
    print('ok',i)
live=page_get(D,P)['content']; open('tracker-live-after.md','w',encoding='utf-8').write(live)
d=[x for x in difflib.ndiff(n(src),n(live)) if x[0] in '+-']
print('diff vs before:',len(d)); print(' '.join(x[2:] for x in d))
