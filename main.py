#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from api import *

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
            "You can send up to 300 emails/day from this sandbox server. "
    m = Mailgun()
    result = m.send(to,subject,msg)
    return render_template("index.html", email=result.status_code)


@app.route("/weather", methods=['POST'])
def weather():
    w = Weather()
    form_data = request.form
    name = form_data['city']
    result = w.weatherByCity(name).json()
    print result
    temp = result['main']['temp']
    city = result['name']
    country = result['sys']['country']
    weather = result['weather'][0]['main']
    print temp, city, country, weather
    msg = u"It's {}ºC in {} {}, and the sky is {} ".format(temp, city, country, weather)
    return render_template("index.html", weather=msg)

@app.route("/tweets", methods=['POST'])
def twitter():
    t = Twitter()
    form_data = request.form
    tag = form_data['tag']
    result = t.getTweetsForTag(tag)
    tweets = []
    for tweet in result:
        tweets.append(u"{} - {}".format(tweet.user.name,tweet.text))
    return render_template("index.html", tweets=tweets)


if __name__ == "__main__":
    app.run()