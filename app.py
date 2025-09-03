# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker! RASIKH RIAZ tag auto incremented according to the workflow number"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
