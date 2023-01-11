import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT title FROM Films
                            WHERE year BETWEEN 1995 AND 2000 AND genre=(
                        SELECT id FROM genres
                            WHERE title = 'детектив')""").fetchall()
print("\n".join(["".join([str(y) for y in x]) for x in result]))
con.close()
