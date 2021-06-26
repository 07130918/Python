import sqlite3

# conn = sqlite3.connect('test_sqlite3.db')
conn = sqlite3.connect('memory')
curs = conn.cursor()

curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')

curs.execute('INSERT INTO persons(name) values("Mike")')
curs.execute('INSERT INTO persons(name) values("Kota")')
curs.execute('INSERT INTO persons(name) values("Jon")')

curs.execute('UPDATE persons set name = "Michel" WHERE name = "Mike"')

curs.execute('DELETE FROM persons WHERE name = "Michel"')

curs.execute('SELECT * FROM persons')
print(curs.fetchall())

curs.execute('DROP TABLE persons')

conn.commit()
curs.close()
conn.close()
