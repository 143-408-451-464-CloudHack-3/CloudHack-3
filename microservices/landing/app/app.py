from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


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

@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    if number_1 == None:
        number_1 = '0'
    if number_2 == None:
        number_2 = '0'
    number_1 = int(number_1)
    number_2 = int(number_2)
    operation = request.form.get('operation')
    result = 0
    if operation == 'add':
        result = add(number_1, number_2)
    elif operation == 'minus':
        result =  minus(number_1, number_2)
    elif operation == 'multiply':
        result = multiply(number_1, number_2)
    elif operation == 'divide':
        result = divide(number_1, number_2)
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

    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )