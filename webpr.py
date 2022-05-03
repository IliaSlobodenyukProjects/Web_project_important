from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('title.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/WaterPolo')
def waterpolo():
    return render_template('ВодноеПоло.html')


@app.route('/Voleyball')
def Voleyball():
    return render_template('Voleyball.html')


@app.route('/AboutUs')
def AboutUs():
    return render_template('about_us.html')

@app.route('/Osoben')
def Osoben():
    return render_template('Особенности.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
