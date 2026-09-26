import sys,re,difflib; sys.path.insert(0,'../s13')
from cu import page_get
live=page_get('2ky45bmy-17253',open('page-id.txt').read().strip())['content']
open('page-live.md','w',encoding='utf-8').write(live)
src=open('../../output/s15/operating-system-page.md',encoding='utf-8').read()
def norm(t):
    t=t.replace('\\','')
    t=re.sub(r'[*_`#>|]',' ',t); t=re.sub(r'^\s*[-:]+\s*$',' ',t,flags=re.M)
    return [w for w in re.split(r'\s+',t) if w and not re.fullmatch(r'[-:]+',w)]
a,b=norm(src),norm(live)
print(len(a),len(b))
d=[x for x in difflib.ndiff(a,b) if x[0] in '+-']
print(len(d)); print(d[:40])
