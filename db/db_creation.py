import sqlite3

def create_lists(query1, path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.execute(query1)
    con.commit()
    con.close()

def insert_data(query1, data, path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.executemany(query1, data) #l3
    con.commit()
    con.close()

def quiz_name(query, path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchall()
    con.close()
    return data

def quiz_info(query, vic, path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.execute(query, vic)
    data = cur.fetchall()
    con.close()
    return data

# create_lists()
# insert_data()