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
        result = requests.get('http://addition:5046/'+str(num1) +'/'+str(num2)).text
    elif operation == 'minus':
        result =  requests.get('http://subtraction:5047/'+str(num1) +'/'+str(num2)).text
    elif operation == 'multiply':
        result = requests.get('http://multiplication:5048/'+str(num1) +'/'+str(num2)).text
    elif operation == 'divide':
        result = requests.get('http://division:5049/'+str(num1) +'/'+str(num2)).text

    flash(f'The result of operation {operation} on {num1} and {num2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )


'''
def add(n1, n2):
    return n1+n2

def minus(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2


def gcd(n1, n2):
    while(n2):
       n1, n2 = n2, n1 % n2
    return n1

def lcm(n1, n2):
    if n1 > n2:
       greater = n1
    else:
       greater = n2
    while(True):
       if((greater % n1 == 0) and (greater % n2 == 0)):
           lcm = greater
           break
       greater += 1
    return lcm

def modulus(n1, n2):
    return n1%n2

def exponent(n1, n2):
    return n1**n2

def greater(n1, n2):
    if n1 > n2:
        return True
    else:
        return False

def less(n1, n2):
    if n1 < n2:
        return True
    else:
        return False

def equal(n1, n2):
    if n1 == n2:
        return True
    else:
        return False
'''

'''
    elif operation == 'GCD':
        result = gcd(number_1, number_2)
    elif operation == 'LCM':
        result = lcm(number_1, number_2)
    elif operation == 'modulus':
        result = modulus(number_1)
    elif operation == 'exponent':
        result = exponent(number_1, number_2)
    elif operation == 'greater':
        result = greater(number_1, number_2)
    elif operation == 'less':
        result = less(number_1, number_2)
    elif operation == 'equal':
        result = equal(number_1, number_2)
'''