from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


<<<<<<< HEAD
class GreaterThan(Resource):
    def get(self,x,y):
        n1 = float(x)
        n2 = float(y)
        if n1 > n2:
            return True
        else:
            return False
api.add_resource(GreaterThan,'/greatthan/<x>/<y>')
=======
class greater_than(Resource):
    def get(self,x,y):
       x=float(x)
       y=float(y)
       if(x>=y):
         return x
       else:
         return y

api.add_resource(grater_than,'/greater_than/<x>/<y>')
>>>>>>> 41b0828ec655feba5624de84a1744a2a7c3486ac

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5054)