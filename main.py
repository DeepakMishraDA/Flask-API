from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

#name = {"name": "Deepak", "age":"age"}

class Hello(Resource):
	def get(self, name, id):
		return {"Hello":name, "your age": id}


api.add_resource(Hello, "/helo/<string:name>/<int:id>")



if __name__ == "__main__":
	app.run(debug=True)
