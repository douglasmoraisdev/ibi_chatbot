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

    _req = request.get_json(silent=True, force=True)
    app.logger.info('Request received: %s' % _req)

    _json_action = _req.get('queryResult').get('action')
    _json_params = _req.get('queryResult').get('parameters')

    _action = Actions()

    response = getattr(_action, _json_action)(_json_params)

    app.logger.info('Response send: %s' % response)
    return jsonify(response)


# run Flask app
if __name__ == "__main__":
    app.run()
