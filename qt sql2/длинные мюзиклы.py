from sqlite3 import connect


def get_result(name):
    con = connect(name)
    cur = con.cursor()
    cur.execute("""UPDATE films SET duration = 100 WHERE genre = 
    (SELECT id FROM genres WHERE title = 'мюзикл') and duration > 100""")
    con.commit()
    con.close()