from flask import Flask, request, jsonify, render_template
import os
import dialogflow
import requests
import json

app = Flask(__name__)

@app.route('/webhook', methods=['GET','POST'])
def get_movie_detail():
    data = request.get_json(silent=True)
    response =  'success!'
    reply = {
        "fulfillmentText": response,
    }

    return jsonify(reply)


# run Flask app
if __name__ == "__main__":
    app.run()
