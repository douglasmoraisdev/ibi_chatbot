import json

from rich_messages.facebook_rich_messages import FacebookRichMessages
from rich_messages.fulfillment_payload import FulfillmentPayload


class City(object):
    """Handle the ask_cells_ask_cells_cidades responses"""

    def __init__(self):
        with open('json_db/json_db.json') as _json_db:
            self.db = json.loads(_json_db.read())

    def barra(self, district):
        """Return Barra Cells by the given district"""

        with open('rich_location_example.json') as _rich_json:
            return json.loads(_rich_json.read())

    def guaiba(self, district):
        """Return Guaiba City Cells by the given district"""

        # response object
        _fulfill = FulfillmentPayload()

        # objects for rich responses
        _fb_rich = FacebookRichMessages()

        # query cells address by district
        _cells_address = self.db.get('cells').get('cities')\
            .get('guaiba').get('districts')\
            .get(district.lower())

        # Iter cell address for facebook payload
        _button_list = []
        for _address in _cells_address:
            _button_list.append(dict(
                type="postback",
                title=_address,
                payload="1"
            ))

        _list_title = "Os endereços das células em Guaíba, %s são: " % district

        # generate facebook rich list
        _facebook_message = _fb_rich.button_list(_list_title, _button_list)

        _message = _fulfill.append('facebook', _facebook_message)

        return _message

    def eldorado(self, district):
        """Return Eldorado Cells by the given district"""

        return 'Ask Eldorado'
