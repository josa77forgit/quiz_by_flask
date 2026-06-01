quiz_create = '''CREATE TABLE IF NOT EXISTS quizes (
    id INTEGER PRIMARY KEY,
    name_quiz VARCHAR)
'''

question_create = '''CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY,
    quest VARCHAR,
    right_ans VARCHAR,
    wr1_ans VARCHAR,
    wr2_ans VARCHAR,
    wr3_ans VARCHAR)
'''

bridge_list = '''CREATE TABLE IF NOT EXISTS bridge (
    id INTEGER PRIMARY KEY,
    quiz_id INTEGER,
    quest_id INTEGER,
    
    FOREIGN KEY (quiz_id) REFERENCES quizes (id),
    FOREIGN KEY (quest_id) REFERENCES questions (id))
'''

quiz_names = '''
    INSERT INTO quizes (name_quiz)
    VALUES (?)
'''

add_quiz = '''
    INSERT INTO questions (
    quest, right_ans, wr1_ans, wr2_ans, wr3_ans)
    VALUES (?, ?, ?, ?, ?)
'''

add_bridge = '''
    INSERT INTO bridge (
    quiz_id, quest_id)
    VALUES (?, ?)
'''

get_quiz = '''
    SELECT * FROM quizes
'''

get_info = '''
    SELECT quest, right_ans, wr1_ans, wr2_ans, wr3_ans FROM questions, bridge
    WHERE bridge.quiz_id == ? and bridge.quest_id == questions.id
'''