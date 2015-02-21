import requests
from flask import Flask
app = Flask(__name__)

api_token = raw_input("Please enter your Yo API Token: ")
port = raw_input("Plese enter port: ")

@app.route("/")
def rolled():
    requests.post(
            "http://api.justyo.co/yo/",
            data={'api_token': api_token, 'username': 'dasilvacontin'}
    )
    return "K"

if __name__ == "__main__":
    app.run("0.0.0.0", int(port))
