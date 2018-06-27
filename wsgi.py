from flask import Flask
import requests

application = Flask(__name__)


@application.route("/")
def hello():
    r = requests.get("http://www.google.com")
    return r.content


if __name__ == "__main__":
    application.run()
