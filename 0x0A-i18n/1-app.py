#!/usr/bin/env python3
"""Module: Basic Flask App"""

from flask import Flask, render_template, refresh
from flask_babel import Babel
from os import getenv


app = Flask(__name__)
babel = Babel(app)
config = Config()
app.config['BABEL_DEFAULT_LOCALE'] = config.get_languages()
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
refresh()


class Config:
    """Class: Configure available languages in our app"""
    LANGUAGES = ["en", "fr"]

    def get_languages():
        """Method: Get Languages"""
        return LANGUAGES


@app.route('/', methods=['GET'], strict_slashes=False)
def home_page():
    """Function: Home Page 0-index.html"""
    return render_template('1-index.html')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)