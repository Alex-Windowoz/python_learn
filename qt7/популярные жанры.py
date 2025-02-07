import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
result = con.execute("""SELECT title FROM genres WHERE id IN 
        (SELECT genre FROM Films WHERE year IN (2010, 2011))""")

for element in result:
    print(element[0])
con.close()

# films_db.sqlite
