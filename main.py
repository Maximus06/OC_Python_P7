from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! in debug mode'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)