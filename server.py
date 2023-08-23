from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)
@dataclass
class res:
    res:int

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    n1=int(request.json['first'])
    n2=int(request.json['second'])
    return jsonify(result(n1+n2))

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    n1=int(request.json['first'])
    n2=int(request.json['second'])
    return jsonify(result(n1-n2))

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
