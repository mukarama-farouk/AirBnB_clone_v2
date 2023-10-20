#!/usr/bin/python3
"""This module writes a script that starts a web app using Flask
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Displays 'Hello HBNB'"""
    return 'Hello HBNB!'

@app.route('/hbnb')
def display():
    """Displays 'HBNB'"""
    return 'HBNB'

@app.route('/c/<text>')
def display_c(text):
    """Displays 'C ' followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
