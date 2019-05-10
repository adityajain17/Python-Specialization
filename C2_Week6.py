fname = input("Enter file name: ")
fh = open(fname)
counts = dict()
for line in fh:
    line=line.rstrip()
    if(line.startswith('From ')):
        words=line.split()
        req_word=words[-2]
        time=req_word.split(':')
        counts[time[0]]=counts.get(time[0],0)+1
temp_list=list(counts.keys())
temp_list.sort()
for k in temp_list:
    print(k,counts[k])
