import constants
import requests
import tweepy
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import aftership



class Mailgun():
    def send(self, to, subject, msg):
        return requests.post(
            "https://api.mailgun.net/v3/sandbox03a400ad1bbd421da31d9dcd3360f748.mailgun.org/messages",
            auth=("api", constants.MAIL_KEY),
            data={"from": "Mailgun Sandbox <postmaster@sandbox03a400ad1bbd421da31d9dcd3360f748.mailgun.org>",
                  "to": to,
                  "subject": subject,
                  "text": msg})

class Weather():
    def weatherByCity(self, name):
        endpoint = "http://api.openweathermap.org/data/2.5/weather"
        payload = {"q": name, "units": "metric", "appid": constants.WHEATHER_KEY}
        print endpoint, payload
        return requests.get(endpoint, params=payload)

class Twitter():
    def getTweetsForTag(self, tag):
        auth = tweepy.OAuthHandler(consumer_key=constants.TWITTER_CONSUMER_KEY,consumer_secret=constants.TWITTER_CONSUMER_SECRET)
        auth.set_access_token(key=constants.TWITTER_KEY,secret=constants.TWITTER_SECRET)
        api = tweepy.API(auth)
        return api.search(q="Stemettes")

class Foursquare():
    def exploreVenues(self, name):
        '''
        Returns a list of Foursquare recommended venues near the location given by parameter name (e.g. London, St Paul's Cathedral etc.)
        '''
        endpoint = "https://api.foursquare.com/v2/venues/explore"
        params = {"near": name,
                  "section": "food",
                  "limit": 5,
                  "client_id": constants.FOURSQUARE_CLIENT_ID,
                  "client_secret": constants.FOURSQUARE_CLIENT_SECRET,
                  "v": "20160831",
                  "m": "foursquare"}
        return requests.get(endpoint, params=params)

class UberRides():
    session = Session(server_token=constants.UBER_SESSION_TOKEN)
    def getProducts(self, latitude, longitude):

        '''Returns types of cars available for in a specific area'''

        client = UberRidesClient(self.session)
        response = client.get_products(latitude, longitude)
        return response.json.get('products')

class AfterShip():

    aftershipApi = aftership.APIv4(constants.AFTERSHIP_API_KEY)

    def getAllCouriers(self):

        '''Returns the names of couriers Aftership supports'''

        return self.aftershipApi.couriers.all.get()

    def createShipment(self,slug,number,Title):

        '''Returns a dictionary of shipment information '''

        return self.aftershipApi.trackings.post(tracking=dict(slug=slug,tracking_number=number, title="title"))

    def getTrackingInfo(self,slug,number):

        '''Returns the tracking information of a parcel'''

        return self.aftershipApi.trackings.get(slug, number)



