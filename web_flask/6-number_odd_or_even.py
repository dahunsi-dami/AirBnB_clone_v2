#!/usr/bin/python3
"""Starts a Flask web application."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    Displays C and value of text variable,
    and replace underscore in text with space.
    """
    text = text.replace("_", " ")
    return f'C {text}'


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """
    Displays Python and value of text variable,
    and replace underscore in text with space.
    """
    text = text.replace("_", " ")
    return f'Python {text}'


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays `{n} is a number` if n is an integer."""
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays HTML page if n is an integer."""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Displays HTML page if n is an integer,
    and tell if it's an odd or even number.
    """
    if (n % 2 == 0):
        n = f'{n} is even'
    else:
        n = f'{n} is odd'
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
