#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)



@app.route('/')
def index():
    """
    Render the home page.

    Returns:
        str: HTML string containing the title of the application.
    """
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    """
    Print a string to the console and display it in the browser.

    Args:
        text (str): The string to be printed and displayed.

    Returns:
        str: The input text.
    """
    print(text)  # Print to console
    return text  # Display in browser

@app.route('/count/<int:number>')
def count(number):
    """
    Display a range of numbers from 0 to the given number (exclusive).

    Args:
        number (int): The upper bound of the range (exclusive).

    Returns:
        str: HTML string with numbers separated by line breaks.
    """
    result = '\n'.join(str(i) for i in range(number))
    return result + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    """
    Perform a mathematical operation on two numbers.

    Args:
        num1 (int): The first number.
        operation (str): The operation to perform (+, -, *, div, or %).
        num2 (int): The second number.

    Returns:
        str: A string representation of the mathematical operation and its result.
    """
    if operation == '+':
        result = num1 + num2
        
    elif operation == '-':
        result = num1 - num2
        
    elif operation == '*':
        result = num1 * num2
        
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else 'Error: Division by zero'
        
    elif operation == '%':
        result = num1 % num2 if num2 != 0 else 'Error: Modulo by zero'
        
    else:
        return 'Invalid operation'
    
    return str (result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
