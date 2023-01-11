import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT DISTINCT title FROM genres
                            WHERE (
                                SELECT year FROM films
                                    WHERE genre=id) BETWEEN 2010 AND 2011"""
                     ).fetchall()
print("\n".join(["".join([str(y) for y in x]) for x in result]))
con.close()
