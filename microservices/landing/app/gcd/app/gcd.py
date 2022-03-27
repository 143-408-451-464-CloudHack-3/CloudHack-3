from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


<<<<<<< HEAD
class GCD(Resource):
    def get(self,x,y):
        n1 = float(x)
        n2 = float(y)
        while(n2):
            n1, n2 = n2, n1 % n2
        return n1

api.add_resource(GCD,'/gcd/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5053)
=======
class Gcd(Resource):
    def get(self,x,y):
        if x>y:
			small=y
		else:
			small=x
		for i in range(1,small+1):
			if((x%i==0) and (y%i==0)):
				gcd=i
				
		return gcd

api.add_resource(Gcd,'/gcd/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5053)
>>>>>>> 41b0828ec655feba5624de84a1744a2a7c3486ac
