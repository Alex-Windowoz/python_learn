from sqlite3 import connect


def get_result(db_name):
    con = connect(db_name)
    cur = con.cursor()
    cur.execute("""DELETE from films WHERE genre = (SELECT id FROM genres WHERE title = 'комедия')""")
    con.commit()
    con.close()
