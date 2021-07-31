from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    # return "Hello Prahlad Inala"
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
