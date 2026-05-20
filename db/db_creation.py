import sqlite3
import queries
import questions

def create_lists():
    con = sqlite3.connect("test_baze.db")
    cur = con.cursor()
    cur.execute(queries.quiz_create)
    cur.execute(queries.question_create)
    cur.execute(queries.bridge_list)
    con.commit()
    con.close()

def insert_data():
    con = sqlite3.connect("test_baze.db")
    cur = con.cursor()
    cur.executemany(queries.quiz_names, questions.l3)
    cur.executemany(queries.add_quiz, questions.l)
    cur.executemany(queries.add_quiz, questions.l2)
    cur.executemany(queries.add_bridge, questions.l5)
    con.commit()
    con.close()

create_lists()
insert_data()