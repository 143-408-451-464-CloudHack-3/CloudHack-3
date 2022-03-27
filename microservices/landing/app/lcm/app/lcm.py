from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

<<<<<<< HEAD

class LCM(Resource):
    def get(self,x,y):
        x = float(x)
        y = float(y)
        if x > y:
            greater = x
        else:
            greater = y
        while(True):
            if((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
        return lcm

api.add_resource(LCM,'/lcm/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5055)
=======
class Lcm(Resource):
    def get(self,x,y):
        if x>y:
            greater=x
        else:
            greater=y
        while(True):
            if ((greater % x==0) and (greater % y==0)):
                lcm=greater
                break
            greater+=1
            
        return lcm

api.add_resource(Lcm,'/lcm/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5055)
	
>>>>>>> 41b0828ec655feba5624de84a1744a2a7c3486ac
