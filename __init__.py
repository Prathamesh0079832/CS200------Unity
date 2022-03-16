from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/quiz-on-git')
def question_page():
    global name
    if request.form["Name"] == '':
        name = 'Poweruser!'
    else:
        name = request.form["Name"]
    return render_template('quiz_page.html', username = name)

@app.route('/quiz-on-git/quiz-results')
def final_page():
    global score
    score = 0
    if request.form["q1"] == 'q1o4':
        score+=1
    return render_template('', finalscore = score)

if __name__ == "__main__":
    app.run(debug=True)
