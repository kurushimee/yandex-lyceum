import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT title FROM Films
    WHERE year >= 1997 AND genre IN (
SELECT id FROM genres
    WHERE title IN ("музыка", "анимация"))""").fetchall()

print("\n".join(["".join(x) for x in result]))
con.close()
