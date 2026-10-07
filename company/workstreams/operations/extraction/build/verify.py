"""Step 6 verify for one run: python3 extraction/build/verify.py s08 [chunk ...]"""
import re,glob,json,os,sys,collections
B='/Users/brandonacuna/Desktop/scaling-people:'
run=sys.argv[1]; only=sys.argv[2:]
chunks=[c[0] for c in json.load(open(f'{B}/extraction/build/{run}/run.json'))['chunks']]
if only: chunks=[c for c in chunks if c in only]
defined=set()
for t in glob.glob(B+'/manual/*/tasks.md'):
    defined|=set(re.findall(r'^### (\d+(?:\.\d+)+)',open(t).read(),re.M))
prefixes={d.rsplit('.',1)[0] for d in defined}
need=['book.md','considerations.md','decisions.md','mapping.md','session.md','tasks.md','notes']
pats=['—',r'\bguests?\b','Recommended','Founder-gated','Chef-gated','Team-filled','Good Energy',r'\bDosi\b','Luxx']
ok=True
for c in chunks:
    d=glob.glob(f'{B}/manual/{c}-*/')[0]; issues=[]
    miss=[n for n in need if not os.path.exists(d+n)]
    if miss: issues.append(('missing',miss))
    for f in glob.glob(d+'*.md'):
        s=open(f).read(); fn=os.path.basename(f)
        for p in pats:
            n=len(re.findall(p,s,re.I if 'guest' in p else 0))
            if n and not (fn=='mapping.md' and p not in ('—',r'\bguests?\b')): issues.append((fn,p,n))
        if fn!='mapping.md' and re.search(r'^#+ .*\bRatify',s,re.M): issues.append((fn,'Ratify title'))
        refs=set(re.findall(r'\b([0-6]\.\d{1,2}\.\d{1,2})\b',s))
        und=sorted(r for r in refs if r not in defined and r.rsplit('.',1)[0] in prefixes)
        if und: issues.append((fn,'undefined refs',und))
    print(c,'OK' if not issues else issues); ok&=not issues
items=re.findall(r'^### (\S+) \|',open(f'{B}/extraction/build/{run}/old-items.md').read(),re.M)
cnt=collections.Counter()
for m in glob.glob(B+'/manual/*/mapping.md'):
    for i in set(re.findall(r'^\|\s*([0-9a-z]{9,11})\s*\|',open(m).read(),re.M)): cnt[i]+=1
un=[i for i in items if cnt[i]==0]; dup=[i for i in items if cnt[i]>1]
print(run,'items',len(items),'unmapped',un,'multi',dup)
