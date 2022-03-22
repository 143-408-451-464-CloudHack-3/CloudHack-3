from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


@app.route('/', methods=['POST', 'GET'])
def index():
    num1 = request.form.get("first")
    num2 = request.form.get('second')
    if num1 == None:
        num1 = '0'
    if num2 == None:
        num2 = '0'
    operation = request.form.get('operation')
    result = 0
    if operation == 'add':
        result = requests.get('http://addition:5046/add/'+str(num1) +'/'+str(num2)).text
    elif operation == 'minus':
        result =  requests.get('http://subtraction:5048/sub/'+str(num1) +'/'+str(num2)).text
    elif operation == 'multiply':
        result = requests.get('http://multiplication:5047/mul/'+str(num1) +'/'+str(num2)).text
    elif operation == 'divide':
        result = requests.get('http://division:5049/div/'+str(num1) +'/'+str(num2)).text
    elif operation == 'GCD':
        result = requests.get('http://gcd:5053/gcd/'+str(num1) +'/'+str(num2)).text
    elif operation == 'LCM':
        result = requests.get('http://lcm:5055/lcm/'+str(num1) +'/'+str(num2)).text
    elif operation == 'modulus':
        result = requests.get('http://modulus:5057/modulus/'+str(num1) +'/'+str(num2)).text
    elif operation == 'exponent':
        result = requests.get('http://exponent:5052/exponent/'+str(num1) +'/'+str(num2)).text
    elif operation == 'greater':
        result = requests.get('http://greatthan:5054/greatthan/'+str(num1) +'/'+str(num2)).text
    elif operation == 'less':
        result = requests.get('http://lessthan:5056/lessthan/'+str(num1) +'/'+str(num2)).text
    elif operation == 'equal':
        result = requests.get('http://equalto:5051/equalto/'+str(num1) +'/'+str(num2)).text

    flash(f'The result of operation {operation} on {num1} and {num2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )


'''
def exponent(n1, n2):
    return n1**n2
'''