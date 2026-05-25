import sqlite3
import main

path = main.app.config.get('DATABASE')

def create_lists(query1, query2, query3):
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    con.commit()
    con.close()

def insert_data(query1, query2, query3, *args):
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.executemany(query1, args[2]) #l3
    cur.executemany(query2, args[0]) #l
    cur.executemany(query2, args[1]) #l2
    cur.executemany(query3, args[4]) #l5
    con.commit()
    con.close()

def quiz_name(query):
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchall()
    con.close()
    return data

# create_lists()
# insert_data()