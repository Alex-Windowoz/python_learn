import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
dur = 85
result = con.execute(f"""SELECT title FROM FILMS WHERE duration <= {dur}""").fetchall()

for element in result:
    print(element[0])
con.close()

# films_db.sqlite
