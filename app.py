from flask import Flask
app = Flask(__name__)


@app.route('/hola')
def hello_world():
    return 'Hello, Docker!'
