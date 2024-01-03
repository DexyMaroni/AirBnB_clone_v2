#!/usr/bin/python3
"""Initializing a flask web app"""

from flask import Flask
app = Flask(__name__)


@app.route("/")
def greeting():
    """A function that prints a welcome message when initiated"""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run
