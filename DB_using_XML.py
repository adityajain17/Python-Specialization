import xml.etree.ElementTree as ET
import sqlite3

file=input('Enter file name : ')
fhand=open(file)
data=fhand.read()
print(data)

tree = ET.fromstring(data)
lst=tree.findall('person')
print(lst)

conn=sqlite3.connect('test.sqlite')
cur=conn.cursor()
cur.execute('drop table if exists student')

cur.execute('create table student (name text,reg text)')


for l in lst:
    cur.execute('insert into student values (?,?)',(l.find('name').text,l.find('reg').text))
    #print((l.find('name').text,l.find('reg').text))
    name=lookup(l,'name')
    reg=lookup(l,'reg')
    print((name,reg))

conn.commit()
cur.close()
conn.close()
