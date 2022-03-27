from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


class Modulus(Resource):
    def get(self,x,y):
<<<<<<< HEAD
        n1 = float(x)
        n2 = float(y)
        return n1%n2

api.add_resource(Modulus,'/modulus/<x>/<y>')
=======
       x=float(x)
       y=float(y)
       return x%y

api.add_resource(Modulus,'/Mod/<x>/<y>')
>>>>>>> 41b0828ec655feba5624de84a1744a2a7c3486ac

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5057)