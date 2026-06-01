import sqlite3
from queries import *
from questions import l, l2, l3, l4, l5
from db_creation import create_lists, insert_data
from main import path

create_lists(quiz_create, path)
create_lists(question_create, path)
create_lists(bridge_list, path)
insert_data(quiz_names, l3, path)
insert_data(add_quiz, l, path)
insert_data(add_quiz, l2, path)
insert_data(add_bridge, l5, path)