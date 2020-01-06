from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/bye')
def bye():
    retJson = {
        'Name':'Szymon',
        'Teleon':62222,
        'Adres':'Honolulu'
    }
    return jsonify(retJson)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)