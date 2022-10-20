import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT DISTINCT year FROM Films
                            WHERE title LIKE 'Х%'""").fetchall()

print("\n".join(["".join([str(y) for y in x]) for x in result]))
con.close()
