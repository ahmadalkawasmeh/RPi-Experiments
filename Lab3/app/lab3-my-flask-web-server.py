from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_sysc3010():
    return "<p>SYSC3010 rocks!</p>"

@app.route('/hello')
def index():
    name = 'X'
    return render_template('hello.html', title='Exercise 3.1', username=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
