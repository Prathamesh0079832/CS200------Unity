from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/quiz-topic', methods=["POST"])
def quiz_topic():
    global name
    if request.form["Name"] == '':
        name = 'Poweruser!'
    else:
        name = request.form["Name"]
    return render_template('quiz_type.html', username = name)

@app.route('/quiz-topic/quiz', methods=["POST"])
def question_page():
    if request.form["quiz_type"] == 'for_git':
        return render_template('quiz_page_git.html', username = name)
    elif request.form["quiz_type"] == 'for_sports':
        return render_template('quiz_page_sports.html', username = name)
    else:
        pass

@app.route('/quiz-topic/quiz/git-quiz-results', methods=["POST"])
def final_page_git():
    global gscore
    gscore = 0
    if request.form["q1g"] == 'q1go4':
        gscore+=1
    if request.form["q2g"] == 'q2go2':
        gscore+=1
    if request.form["q3g"] == 'q3go1':
        gscore+=1
    if request.form["q4g"] == 'q4go3':
        gscore+=1
    if request.form["q5g"] == 'q5go3':
        gscore+=1
    if request.form["q6g"] == 'q6go2':
        gscore+=1
    if request.form["q7g"] == 'q7go1':
        gscore+=1
    if request.form["q8g"] == 'q8go2':
        gscore+=1
    if request.form["q9g"] == 'q9go1':
        gscore+=1
    if request.form["q10g"] == 'q10go3':
        gscore+=1
    return render_template('final_page.html', finalscore = gscore)

@app.route('quiz-topic/quiz/sports-quiz-results', mathods=["POST"])
def final_page_sports():
    global sscore
    sscore = 0
    if request.form["q1s"] == 'q1so3':
        gscore+=1
    return render_template('final_page.html', finalscore = sscore)


if __name__ == "__main__":
    app.run(debug=True)
