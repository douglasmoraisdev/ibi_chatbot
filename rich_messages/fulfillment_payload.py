import json


class FulfillmentPayload():
    """Handle base Fulfillment Payload format"""

    def __init__(self):
        pass

    def append(self, payload_name, payload_message):
        with open('rich_messages/templates/base_fulfillment_messages.json') as\
                _json_fulfillment:
            _base_fulfillment = json.loads(_json_fulfillment.read())

        _base_fulfillment["fulfillmentMessages"][0][
            "payload"][payload_name] = payload_message[payload_name]

        return _base_fulfillment
