from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


class GreaterThan(Resource):
    def get(self,x,y):
        n1 = float(x)
        n2 = float(y)
        if n1 > n2:
            return True
        else:
            return False
api.add_resource(GreaterThan,'/greatthan/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5054)