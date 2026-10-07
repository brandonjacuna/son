import sys,os; sys.path.insert(0,'../s13')
from cu import req, page_append
src=open('../../output/s15/operating-system-page.md',encoding='utf-8').read()
paras=src.split('\n\n'); chunks=[]; cur=''
for p in paras:
    add=(p if not cur else '\n\n'+p)
    if cur and len((cur+add).encode())>24000: chunks.append(cur); cur=p
    else: cur+=add
chunks.append(cur)
assert '\n\n'.join(chunks)==src
os.makedirs('chunks',exist_ok=True)
for i,c in enumerate(chunks,1): open(f'chunks/c{i:02}.md','w',encoding='utf-8').write(c if i==1 else '\n\n'+c)
print(len(chunks),[len(c.encode()) for c in chunks])
if len(sys.argv)>1 and sys.argv[1]=='go':
    title=src.split('\n',1)[0].lstrip('# ').replace('Session 15:','S15:',1)
    if os.path.exists('page-id.txt'): pid=open('page-id.txt').read().strip()
    else:
        r=req('POST','workspaces/90131574430/docs/2ky45bmy-17253/pages',{'name':title,'content':open('chunks/c01.md').read(),'content_format':'text/md'},v='v3')
        pid=r['id']; open('page-id.txt','w').write(pid); print('created',pid,title)
    for i in range(2,len(chunks)+1):
        page_append('2ky45bmy-17253',pid,open(f'chunks/c{i:02}.md',encoding='utf-8').read()); print('appended',i)
