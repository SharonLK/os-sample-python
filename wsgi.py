from flask import Flask
import requests

application = Flask(__name__)


def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n - 1) + F(n - 2)


@application.route("/")
def hello():
    return F(35)


if __name__ == "__main__":
    application.run()
