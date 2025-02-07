import sqlite3

artist_name = input()
con = sqlite3.connect('Chinook_Sqlite.sqlite')
cur = con.cursor()
result = con.execute(f"SELECT track.Name FROM album INNER JOIN artist ON album.artistid = artist.artistid "
                     f"INNER JOIN track ON track.AlbumId = album.AlbumId WHERE artist.name = '{artist_name}'")

result = sorted(result)
for el in result:
    print(el[0])
# music_db.sqlite
# Lenny Kravitz
