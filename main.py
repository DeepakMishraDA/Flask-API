from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
	def get(self):
		return {"Mine":"Shreya"}

api.add_resource(Hello, "/helo")

if __name__ == "__main__":
	app.run(debug=True)
