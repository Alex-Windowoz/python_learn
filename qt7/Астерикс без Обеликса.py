import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
result = con.execute(
    """SELECT title FROM Films WHERE title LIKE '%Астерикс%' AND title NOT LIKE '%Обеликс%'""").fetchall()

for el in result:
    print(el[0])

con.close()
