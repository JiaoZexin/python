from flask import Flask
import time

app=Flask(__name__)

@app.route('/tian')
def index_tian():
    time.sleep(2)
    return "hello tian"

@app.route('/jian')
def index_jian():
    time.sleep(2)
    return "hello jian"

@app.route('/ying')
def index_ying():
    time.sleep(2)
    return "hello ying"

if __name__ == '__main__':
    app.run(threaded=True)