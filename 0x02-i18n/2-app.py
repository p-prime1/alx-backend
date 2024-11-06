#!/usr/bin/env python3
"""get_locale fun determines the best match for supported languages"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Class sets babels default locale to 'en' and timezone to 'UTC'"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)\


babel = Babel(app)


@babel.localeselector
def get_locale():
    """function determines the best match from supported languages in
    config class"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
