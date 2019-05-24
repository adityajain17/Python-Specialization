import json
# a Python object (dict):
fhand=open('countries.txt')
jlist=[]
for c in fhand:
    c=c.strip()
    ob = {"id": "male","active":True,"defaultOption":True,"optionText":c,"optionValue":c}
    t=json.dumps(ob)
    print(t,end=',')
