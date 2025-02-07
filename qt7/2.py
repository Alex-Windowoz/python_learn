import sqlite3

db_name = input()
con = sqlite3.connect(db_name)

cur = con.cursor()
result = cur.execute("""SELECT title FROM Films WHERE title LIKE '%?'""").fetchall()
for title in result:
    print(title[0])
con.close()

# films_db.sqlite
