from flask import *

app = Flask()
@app.route("/")
def index():
    return "This is Flask API test!"
