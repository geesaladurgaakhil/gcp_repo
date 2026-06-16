from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Python App running on GKE tested by Akhil"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
