from sqlite3 import connect


def get_result(name):
    con = connect(name)
    cur = con.cursor()
    cur.execute("""UPDATE films SET duration = duration * 2 
        WHERE genre = (SELECT id FROM genres WHERE title = 'фантастика')""")
    con.commit()
    con.close()
