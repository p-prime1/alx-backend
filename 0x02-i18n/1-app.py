from flask import Flask, render_template
from flask_babel import Babel
"""Module inititalizes contains Config class and instantiates babel"""


class Config:
    """Class sets babels default locale to 'en' and timezone to 'UTC'"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)

babel = Babel(app)
@app.route('/')

def home():
    return render_template('0-index.html')
if __name__ == "__main__":
    app.run(debug=True)
