import sys,re,os,difflib; sys.path.insert(0,'../s13')
from cu import page_append,page_replace,page_get
src=open('tracker-after.md',encoding='utf-8').read()
parts=re.split(r'(?=\n\n)|(?=\n\*   )',src)
chunks=[];cur=''
for p in parts:
    if cur and len((cur+p).encode())>12000: chunks.append(cur); cur=p
    else: cur+=p
chunks.append(cur); assert ''.join(chunks)==src
os.makedirs('ledger-chunks',exist_ok=True)
for i,c in enumerate(chunks,1): open(f'ledger-chunks/l{i:02}.md','w',encoding='utf-8').write(c)
print(len(chunks),[len(c.encode()) for c in chunks])
D,P='2ky45bmy-17233','2ky45bmy-30353'
page_replace(D,P,chunks[0]); print('replaced 1')
for i,c in enumerate(chunks[1:],2): page_append(D,P,c); print('appended',i)
live=page_get(D,P)['content']; open('tracker-live-after.md','w',encoding='utf-8').write(live)
def n(t): return re.sub(r'[\\*`_#>|]',' ',t).split()
a,b=n(src),n(live); d=[x for x in difflib.ndiff(a,b) if x[0] in '+-']
print(len(a),len(b),len(d),d[:20])
