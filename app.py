import os
import requests
import json
import dialogflow
from actions import Actions

from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def webhook():

    req = request.get_json(silent=True, force=True)
    json_action = req.get('queryResult').get('action')

    print('---req %s' % req)
    print('---json_action %s' % json_action)

    action = Actions()

    response = getattr(action, json_action)(req)

    #response =  'success!'
    reply = {
        "fulfillmentText": response,
    }

    return jsonify(reply)


# run Flask app
if __name__ == "__main__":
    app.run()
