import sqlite3

conn=sqlite3.connect('Python_C3.db')
cur=conn.cursor()
print(cur)


cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
('Thunderstruck', 20))
print(cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
('My Way', 15)))
conn.commit()
cur.execute('SELECT * FROM Tracks')
for row in cur:
    print(row)
cur.close();
conn.close();
