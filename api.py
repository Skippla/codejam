import constants
import requests
import tweepy

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
