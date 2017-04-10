#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask import render_template
from flask import request
from api import *

template_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=template_dir)
import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
        username='5afebac5-b78a-41ff-af20-9139caae644e',
        password='tMxm0cxx0kwV',
        version='2016-09-20')
context = {}
    
@app.route("/")
def index():
    print 'INDEX'
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
    form_data = request.form
    emails = [e.strip() for e in form_data['emailinput'].split(',')]
    print emails
    subject = "Hello Maria"
    msg = "Congratulations Maria, you just sent an email with Mailgun!  You are truly awesome!  " \
            "You can send up to 300 emails/day from this sandbox server. "
    m = Mailgun()
    result = m.send(emails,subject,msg)
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




@app.route("/foursquare", methods=['POST'])
def foursquare():
    f = Foursquare()
    form_data = request.form
    location = form_data['location']
    result = f.exploreVenues(location).json()
    venues = []
    for item in result['response']['groups'][0]['items']:
        name = item['venue']['name']
        rating = item['venue']['rating']
        address = ", ".join(item['venue']['location']['formattedAddress'])
        venues.append(u"Name: {}, Rating: {}, Address: {}".format(name, rating, address))
    return render_template("index.html", venues=venues)

@app.route("/uber", methods=['POST'])
def uber_product():
    u = UberRides()
    form_data = request.form
    latitude = form_data['latitude']
    longitude = form_data['longitude']
    products = u.getProducts(latitude, longitude)
    return render_template("index.html", products=products)

@app.route("/aftership", methods=['POST'])
def aftership_Create_Shipment():
    a = AfterShip()
    form_data = request.form
    slug = form_data['slug']
    number = form_data['number']
    title = form_data['title']
    ShipmentInfo = a.createShipment(slug,number,title)
    return render_template("index.html", ShipmentInfo=ShipmentInfo)

@app.route("/game", methods=['POST'])
def game():
    print 'GAME'
    global context, conversation
    workspace_id = '54555911-c3e9-475d-bb16-a726d3b44dc8'
    form_data = request.form
    answer = form_data['answer']
    result = conversation.message(workspace_id=workspace_id, message_input={'text': answer},context=context)
    context=result['context']
    response = result['output']['text'][0]
    print(response)
    return render_template("game.html",response=response)


@app.route("/watson", methods=['POST'])
def watson():
    global context, conversation
    workspace_id = '54555911-c3e9-475d-bb16-a726d3b44dc8'
    form_data = request.form
    answer = form_data['answer']
    result = conversation.message(workspace_id=workspace_id, message_input={'text': answer},context=context)
    context=result['context']
    response = result['output']['text'][0]
    print(response)
    return render_template("game.html",response=response)

#app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
if __name__ == "__main__":
    app.run()