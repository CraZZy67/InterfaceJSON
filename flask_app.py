from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return "46c97ca2"
    else:
        return "<p><b>БОТ ВКЛЮЧЕН</b></p>"
