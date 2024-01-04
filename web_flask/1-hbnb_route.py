#!/usr/bin/python3

""" A script thatstarts a web application and has two routes. """

from flask import Flask

app = Flask(__name__)


@app.route("/")
def greeting():
    """A function that prints a welcome message when initiated"""
    return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
    """ A function that prints HBNB """
    return "HBNB"

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host= '0.0.0.0', port = 5000)
