#!/usr/bin/python3
"""This module contains a script that starts a web app using Flask
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

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
