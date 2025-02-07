from sqlite3 import connect


def get_result(name):
    con = connect(name)
    cur = con.cursor()
    cur.execute("""DELETE FROM films WHERE title LIKE 'Я%' and title LIKE '%а'""")
    con.commit()
    con.close()
