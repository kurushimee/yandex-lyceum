import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute("""DELETE FROM films
                    WHERE duration > 90 AND year < 2000 AND genre=(
                        SELECT id FROM genres
                            WHERE title = 'фантастика')""").fetchall()
    con.commit()
    con.close()
