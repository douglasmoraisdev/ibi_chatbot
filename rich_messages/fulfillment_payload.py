import json

from flask import Flask

import config.logconfig

app = Flask(__name__)


class FulfillmentPayload():
    """Handle base Fulfillment Payload format"""

    def __init__(self):
        with open('rich_messages/templates/base_fulfillment_messages.json') as\
                _json_fulfillment:
            _base_fulfillment = json.loads(_json_fulfillment.read())

        self.output = _base_fulfillment

        pass

    def append(self, payload_name, payload_message):

        self.output["fulfillmentMessages"][0][
            "payload"][payload_name] = payload_message[payload_name]

        return self.output
