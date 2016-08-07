from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<name>")
def hello(name):
    return render_template("index.html",name=name.title())

@app.route("/signup", methods=['POST'])
def sign_up():
    form_data = request.form
    name = form_data['name']
    print name
    print form_data['email']
    return render_template("signup.html",name=name.title())

if __name__ == "__main__":
    app.run()