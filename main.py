from flask import Flask, render_template, request, redirect, url_for, session
from new_db.db_creation import quiz_name, quiz_info
from new_db.queries import get_quiz, get_info
import random
import os

DATABASE = "/quiz_by_flask/test_base.db"
SECRET_KEY = "value"
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE = os.path.join(app.root_path, 'test_base.db')))
path = app.config.get('DATABASE')

@app.route('/', methods=['POST', 'GET'])
def index():
    names = quiz_name(get_quiz, path)
    if request.method == 'POST':
        res = request.form.get("list")
        information = quiz_info(get_info, res, path)
        session['questions'] = information
        session['quiz_id'] = res
        session['cnt'] = 0
        session['user_ans'] = []
        return redirect(url_for('test'))
    return render_template(template_name_or_list='index.html', quiz_list=names, title='Викторина')

@app.route('/second', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        res2 = request.form.get("answer")
        session['user_ans'].append(res2)
        session['cnt'] += 1
    if session['cnt'] < len(session['questions']):
        current_quest = session['questions'][session['cnt']]
        quest = current_quest[0]
        answ = list(current_quest[1:])
        random.shuffle(answ)
    else:
        return redirect(url_for('result'))
    return render_template(template_name_or_list='test.html', question=quest, answer=answ, title='Викторина')

@app.route('/result', methods=['POST', 'GET'])
def result():
    right_a = [question[1] for question in session['questions']]
    user_right = []
    user_wrong = []
    for i in session['user_ans']:
        if i in right_a:
            user_right.append(i)
        else:
            user_wrong.append(i)
    return render_template(template_name_or_list='result.html', all_quest=session['questions'], user_ans=session['user_ans'], right_ans=right_a, title='Викторина')

if __name__ == '__main__':
    app.run(debug = True)