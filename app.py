from flask import request
from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/hi")
def api_root():
    return 'Welcome to the chatbot from hell'


