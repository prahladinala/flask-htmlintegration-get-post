from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def welcome():
    # return "Hello Prahlad Inala"
    return render_template('getandpost.html')


@app.route('/pass/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html', result=res)


@app.route('/fail/<int:score>')
def fail(score):
    return "<h2 style='color: red'>The Person has failed and the marks is " + str(score) + "</h2>"

# RESULT CHECKER


@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=marks))

# RESULT CHECKER HTML PAGE


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4
    res = ""
    # if total_score >= 50:
    #     res = "success"
    # else:
    #     res = "fail"
    # dynamic url generation
    return redirect(url_for("success", score=total_score))


if __name__ == "__main__":
    app.run(debug=True)
