from sqlite3 import connect


def get_result(db_name):
    con = connect(db_name)
    cur = con.cursor()
    cur.execute("""UPDATE films SET duration = '42' WHERE duration = ''""")
    con.commit()
    con.close()