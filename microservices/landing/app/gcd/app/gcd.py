from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


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
