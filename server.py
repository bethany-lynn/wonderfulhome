from flask import Flask
from jinja2 import StrictUndefined
from model import *

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """view homepage"""

    return "Hello, world!"

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)