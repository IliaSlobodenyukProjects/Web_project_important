from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('title.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/AboutUs')
def AboutUs():
    return 'AboutUs'


@app.route('/name')
def name():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
