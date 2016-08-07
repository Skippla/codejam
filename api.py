import constants
import requests

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
        payload = {"q": name, "appid": constants.WHEATHER_KEY}
        print endpoint, payload
        return requests.get(endpoint, params=payload)