#!/usr/bin/env python3
"""Get_locale fun determines the best match for supported languages
    Config consist of supported languages and Locale timezone"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Class sets babels default locale to 'en' and timezone to 'UTC'"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


babel = Babel()


def get_locale():
    """function determines the best match from supported languages in
    config class"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def home():
    """Renders the the html fiel"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)