import re
file=input('Enter the file name: ')
hand=open(file)
c=0
g=[]
s=0
for line in hand:
    line=line.strip()
    x=re.findall('[0-9]+',line)
    if len(x)>0:
        for i in x:
            t=int(i)
            s=s+t
        c=c+len(x)

print(s)
