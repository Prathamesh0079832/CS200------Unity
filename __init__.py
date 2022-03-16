from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/quiz-on-git', methods=["POST"])
def question_page():
    global name
    if request.form["Name"] == '':
        name = 'Poweruser!'
    else:
        name = request.form["Name"]
    return render_template('quiz_page.html', username = name)

@app.route('/quiz-on-git/quiz-results', methods=["POST"])
def final_page():
    global score
    score = 0
    if request.form["q1"] == 'q1o4':
        score+=1
    if request.fotm["q2"] == 'q2o2':
        score+=1
    if request.form["q3"] == 'q3o1':
        score+=1
    if request.form["q4"] == 'q4o3':
        score+=1
    if request.form["q5"] == 'q5o3':
        score+=1
    if request.form["q6"] == 'q6o2':
        score+=1
    if request.form["q7"] == 'q7o1':
        score+=1
    if request.form["q8"] == 'q8o2':
        score+=1
    if request.form["q9"] == 'q9o1':
        score+=1
    if request.form["q10"] == 'q10o3':
        score+=1
    return render_template('final_page.html', finalscore = score)

if __name__ == "__main__":
    app.run(debug=True)
