import sqlite3
from queries import *
from questions import l, l2, l3, l4, l5
from db_creation import create_lists, insert_data

create_lists(quiz_create, question_create, bridge_list)
insert_data(quiz_names, add_quiz, add_bridge, l, l2, l3, l4, l5)