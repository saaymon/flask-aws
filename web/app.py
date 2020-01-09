from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

#test1

def checkPostedData(postedData, functionName):
    if (functionName == "add"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200

class Add(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "add")
        if (status_code != 200):
            retJson = {
                "Message":"Error ",
                'Status Code': 301
            }
            return jsonify(retJson)
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x+y
        retMap = {
            'Sum': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Subtract(Resource):
    pass

class Multiply(Resource):
    pass

class Divide(Resource):
    pass

api.add_resource(Add, "/add")

@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/add_two_numes', methods=["POST"])
def add_two_numes():
    dataDict = request.get_json()
    x = dataDict["x"]
    y = dataDict["y"]
    z = x + y
    retJson = {
        "z":z
    }
    return jsonify(retJson)


@app.route('/bye')
def bye():
    retJson = {
        'Name': 'Szymon',
        'Teleon': 62222,
        'Adres': 'Honolulu'
    }
    return jsonify(retJson)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
