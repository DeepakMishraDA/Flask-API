from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"this":{ "who":"Deepak", "age":18},
"that": {"who": "Shreya","age": 16}}

class Hello(Resource):
	def get(self, name):
		return names[name]


api.add_resource(Hello, "/helo/<string:name>")



if __name__ == "__main__":
	app.run(debug=True)

"second change"