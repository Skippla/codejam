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

# class Mailgun():
#     def send(self, to, subject, msg):
#         return requests.post(
#             "https://api.mailgun.net/v3/sandbox03a400ad1bbd421da31d9dcd3360f748.mailgun.org/messages",
#             auth=("api", "key-b6a4d8ce526a19f0013a0c9dba7ae48d"),
#             data={"from": "Mailgun Sandbox <postmaster@sandbox03a400ad1bbd421da31d9dcd3360f748.mailgun.org>",
#                   "to": to,
#                   "subject": subject,
#                   "text": msg})


if __name__ == "__main__":
    app.run()