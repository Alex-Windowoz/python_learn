from sqlite3 import connect


def get_result(name):
    con = connect(name)
    cur = con.cursor()
    cur.execute("""DELETE FROM films WHERE duration >= 90
    and genre = (SELECT id FROM genres WHERE title = 'боевик')""")
    con.commit()
    con.close()
