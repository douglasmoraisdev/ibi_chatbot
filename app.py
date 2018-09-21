import os
import requests
import json
import dialogflow
from actions.actions import Actions

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def webhook():
    """Main entry endpoint of the webhook"""

    _req = request.get_json(silent=True, force=True)
    print(_req)
    _json_action = _req.get('queryResult').get('action')
    _json_params = _req.get('queryResult').get('parameters')

    _action = Actions()

    response = getattr(_action, _json_action)(_json_params)

    print(response)

    return jsonify(response)

    '''
    reply = {
        "fulfillmentText": response,
    }

    # print(_req)
    return jsonify(reply)
    '''


# run Flask app
if __name__ == "__main__":
    app.run()
