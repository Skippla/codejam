
import requests

class Mailgun():
    def send(self, to, subject, msg):
        return requests.post(
            "https://api.mailgun.net/v3/sandbox03a400ad1bbd421da31d9dcd3360f748.mailgun.org/messages",
            auth=("api", "key-b6a4d8ce526a19f0013a0c9dba7ae48d"),
            data={"from": "Mailgun Sandbox <postmaster@sandbox03a400ad1bbd421da31d9dcd3360f748.mailgun.org>",
                  "to": to,
                  "subject": subject,
                  "text": msg})