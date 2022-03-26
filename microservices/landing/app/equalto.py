from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


class Lesser_than(Resource):
    def get(self,x,y):
        if float(x) == float(y):
			return 1
		else:
			return 0

api.add_resource(Lesser_than,'/lessthan/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5056)
