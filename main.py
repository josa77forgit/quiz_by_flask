from flask import Flask, render_template, request, redirect, url_for, session
from db.questions import l3, l4

app = Flask(__name__)
app.config['SECRET_KEY'] = 'value'

@app.route('/', methods=['POST', 'GET'])
def index():
    quiz = ['1', '2']
    if request.method == 'POST':
        res = request.form.get("list")
        print(l3.index(res))
        session['quiz_id'] = l3.index(res)
        session['cnt'] = 0
        session['right_ans'] = []
        return redirect(url_for('test'))
    return render_template(template_name_or_list='index.html', quiz_list=l3, title='Викторина')

@app.route('/second', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        res2 = request.form.get("answer")
        session['right_ans'].append(res2)
        session['cnt'] += 1
    if session['cnt'] < len(l4[session['quiz_id']]):
        ind = l4[session['quiz_id']][session['cnt']]
        quest = ind[0]
        answ = ind[1:]
    else:
        return redirect(url_for('result'))
    return render_template(template_name_or_list='test.html', question=quest, answer=answ, title='Викторина')

@app.route('/result', methods=['POST', 'GET'])
def result():
    print(session['right_ans'])
    right_a = [question[1] for question in l4[session['quiz_id']]]
    print(right_a)
    user_right = []
    user_wrong = []
    for i in session['right_ans']:
        if i in right_a:
            user_right.append(i)
        else:
            user_wrong.append(i)
    print(user_right)
    print(user_wrong)
    return render_template(template_name_or_list='result.html', ans1=user_right, ans2=user_wrong, title='Викторина')

app.run(debug=True)