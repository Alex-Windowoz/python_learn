from sqlite3 import connect


def get_result(name):
    con = connect(name)
    cur = con.cursor()
    cur.execute("""UPDATE films SET duration = duration / 3 WHERE year = 1973""")
    con.commit()
    con.close()
