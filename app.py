from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World! This is my dev branch that i am pushing to staging"


@app.route("/review_status")
def review():
	return "dev branch has been reviewed"

@app.route("/new_route")
def new_route():
	return "this is a new route"
    return "Hello World! This is on prod"