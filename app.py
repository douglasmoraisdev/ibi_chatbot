import os
import requests
import json

from flask import Flask, request, jsonify, render_template

from actions.actions import Actions
import config.logconfig

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def webhook():
    """Main entry endpoint of the webhook"""

    # format the request in json format
    _req = request.get_json(silent=True, force=True)
    app.logger.info('Request received: %s' % _req)

    # get action and input parameters
    _json_action = _req.get('queryResult').get('action')
    _json_params = _req.get('queryResult').get('parameters')

    # get output parameters(followup) if exists
    if 'outputContexts' in _req.get('queryResult'):
        _json_outputContexts = _req.get('queryResult').get('outputContexts')
    else:
        _json_outputContexts = None

    _action = Actions()

    # make the response
    response = getattr(_action, _json_action)(_json_params, _json_outputContexts)

    app.logger.info('Response send: %s' % response)
    return jsonify(response)


# run Flask app
if __name__ == "__main__":
    app.run()
