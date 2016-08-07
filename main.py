from flask import Flask
from flask import render_template
from flask import request
from api import Mailgun

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


@app.route("/email", methods=['POST'])
def email():
    to = "Maria <maria.arinbjarnar@gmail.com>",
    subject = "Hello Maria",
    msg = "Congratulations Maria, you just sent an email with Mailgun!  You are truly awesome!  " \
            "You can see a record of this email in your logs: https://mailgun.com/cp/log .  " \
            "You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free."
    m = Mailgun()
    result = m.send(to,subject,msg)
    print result
    return render_template("index.html", email=result)

if __name__ == "__main__":
    app.run()