fname = input("Enter file name: ")
fh = open(fname)
count=0
val=0.0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        val=val+float(line[line.find('.')-1:len(line)])
        count=count+1
avg=val/count
print('Average spam confidence:',avg)
