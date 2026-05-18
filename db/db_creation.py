import sqlite3
import queries

def create_lists():
    con = sqlite3.connect("test_baze.db")
    cur = con.cursor()
    cur.execute(queries.quiz_create)
    cur.execute(queries.question_create)
    cur.execute(queries.bridge_list)
    con.commit()
    con.close()

create_lists()