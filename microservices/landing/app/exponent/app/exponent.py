from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


<<<<<<< HEAD
class Exponent(Resource):
    def get(self,x,y):
        n1 = float(x)
        n2 = float(y)
        return n1**n2

api.add_resource(Exponent,'/exponent/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5052)
=======
class Addition(Resource):
    def get(self,x,y):
        x = float(x)
        y = float(y)
        return x**y

api.add_resource(Addition,'/add/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5046)
>>>>>>> 41b0828ec655feba5624de84a1744a2a7c3486ac
