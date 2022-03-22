from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class Multiplication(Resource):
    def get(self,x,y):
        return x*y

api.add_resource(Multiplication,'/mul/<float:x>/<float:y>')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5047)

