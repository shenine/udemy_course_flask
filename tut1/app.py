from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


def check_posted(postedData, functionName):
	if (functionName == "add" or functionName == "subtract" or functionName == "multiply"):
		if "x" not in postedData or "y" not in postedData:
			return 301
		else:
			return 200
	elif (functionName == "divide"):
		if "x" not in postedData or "y" not in postedData:
			return 301
		elif int(postedData["y"]) == 0:
			return 302
		else:
			return 200

class Add(Resource):
	def post(self):
		# if I'm here Add was requested using POST

		#step 1: get posted data
		postedData = request.get_json()

		#step 1b: verify posted data
		status_code = check_posted(postedData, "add")
		if (status_code != 200):
			retJson = {
				"Message": "An error occured",
				"status Code": status_code
			}
			return jsonify(retJson)

		#if I am here status_code == 200
		x = postedData['x']
		y = postedData['y']
		x = int(x)
		y = int(y)
		#step 2: add data
		ret = x+y
		#step 3: create response
		retMap = {
			'Message':ret,
			'Status Code':200
		}
		return jsonify(retMap)

class Subtract(Resource):
	def post(self):
		# if I'm here Add was requested using POST

		#step 1: get posted data
		postedData = request.get_json()

		#step 1b: verify posted data
		status_code = check_posted(postedData, "subtract")
		if (status_code != 200):
			retJson = {
				"Message": "An error occured",
				"status Code": status_code
			}
			return jsonify(retJson)

		#if I am here status_code == 200
		x = postedData['x']
		y = postedData['y']
		x = int(x)
		y = int(y)
		#step 2: subtract data
		ret = x-y
		#step 3: create response
		retMap = {
			'Message':ret,
			'Status Code':200
		}
		return jsonify(retMap)

class Multiply(Resource):
	def post(self):
		# if I'm here Add was requested using POST

		#step 1: get posted data
		postedData = request.get_json()

		#step 1b: verify posted data
		status_code = check_posted(postedData, "multiply")
		if (status_code != 200):
			retJson = {
				"Message": "An error occured",
				"status Code": status_code
			}
			return jsonify(retJson)

		#if I am here status_code == 200
		x = postedData['x']
		y = postedData['y']
		x = int(x)
		y = int(y)
		#step 2: multiply data
		ret = x*y
		#step 3: create response
		retMap = {
			'Message':ret,
			'Status Code':200
		}
		return jsonify(retMap)

class Divide(Resource):
	def post(self):
		# if I'm here Add was requested using POST

		#step 1: get posted data
		postedData = request.get_json()

		#step 1b: verify posted data
		status_code = check_posted(postedData, "divide")
		if (status_code != 200):
			retJson = {
				"Message": "An error occured",
				"status Code": status_code
			}
			return jsonify(retJson)

		#if I am here status_code == 200
		x = postedData['x']
		y = postedData['y']
		x = int(x)
		y = int(y)
		#step 2: divide data
		ret = (x*1.0)/y
		#step 3: create response
		retMap = {
			'Message':ret,
			'Status Code':200
		}
		return jsonify(retMap)

#	def get(self):
#		# if I'm here Add was requested using GET
#	def put(self):
#		# if I'm here Add was requested using PUT
#	def delete(self):
#		# if I'm here Add was requested using DELETE

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")

#@app.route('/')
#def hello_world():
#	return "Hello World"
#
#@app.route('/add_two_nums', methods = ['POST', 'GET'])
#def add_two_nums():
#	#Get x and y from posted data
#	dataDict = request.get_json()
#
#	if "y" not in dataDict:
#		return "ERROR", 305
#
#	#Add x+y and store in z
#	x = dataDict["x"]
#	y = dataDict["y"]
#	z = x + y
#
#	#Prepare JSON with 'z':z
#	retJson = {
#		"z":z
#	}
#
#	return jsonify(retJson), 200

if __name__=="__main__":
	app.run(debug=True)