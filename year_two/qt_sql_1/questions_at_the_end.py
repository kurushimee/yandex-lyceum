import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT title FROM Films
    WHERE title LIKE '%?'""").fetchall()

print("\n".join(["".join(x) for x in result]))
con.close()
