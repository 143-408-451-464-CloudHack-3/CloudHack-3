from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


<<<<<<< HEAD
class LessThan(Resource):
    def get(self,x,y):
        x = float(x)
        y = float(y)
        if x < y:
            return True
        else:
            return False

api.add_resource(LessThan,'/lessthan/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5056)
=======
class Lesser_than(Resource):
    def get(self,x,y):
        if float(x)>float(y):
			return y
		else:
			return x

api.add_resource(Lesser_than,'/lessthan/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5056)
>>>>>>> 41b0828ec655feba5624de84a1744a2a7c3486ac
