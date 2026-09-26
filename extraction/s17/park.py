import sys,re,difflib; sys.path.insert(0,'../s13')
from cu import page_append,page_replace,page_get
D,P='2ky45bmy-17233','2ky45bmy-30353'
src=page_get(D,P)['content']; open('tracker-before.md','w',encoding='utf-8').write(src)
anchor='> Sŏn. Scaling People, session 17. ClickUp task `86ajgmk27`. Begin.\n'
assert src.count(anchor)==1
note=('\n**Gate check, 2026-09-25.** Session 17 was opened and parked before any work. The gate could not be confirmed: '
 '`86ajgn2z5` returns "Team not authorized" to both the connector and the REST token, and it does not surface in workspace search. '
 'Brandon ruled that the methodology has not landed. Nothing was written, filed, or closed. '
 'Resume only when Brandon confirms the methodology has landed and names where it can be read, since assembly applies its rules to every page.\n')
new=src.replace(anchor,anchor+note)
open('tracker-after.md','w',encoding='utf-8').write(new)
parts=re.split(r'(?=\n\n)|(?=\n\*   )',new); chunks=[];cur=''
for p in parts:
    if cur and len((cur+p).encode())>12000: chunks.append(cur); cur=p
    else: cur+=p
chunks.append(cur); assert ''.join(chunks)==new
page_replace(D,P,chunks[0])
for c in chunks[1:]: page_append(D,P,c)
live=page_get(D,P)['content']; open('tracker-live-after.md','w',encoding='utf-8').write(live)
n=lambda t: re.sub(r'[\\*`_#>|]',' ',t).split()
d=[x for x in difflib.ndiff(n(src),n(live)) if x[0] in '+-']
print(len(chunks),'diff tokens:',len(d)); print(' '.join(x[2:] for x in d))
