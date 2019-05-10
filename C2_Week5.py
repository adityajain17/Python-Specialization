fname = input("Enter file name: ")
fh = open(fname)
counts=dict()
for line in fh:
    if line.startswith('From '):
        words=line.rstrip().split()
        counts[words[1]]=counts.get(words[1],0)+1
eid=None
ec=None
for k,v in counts.items():
    if ec is None or v > ec:
        eid=k
        ec=v
print(eid,ec)
