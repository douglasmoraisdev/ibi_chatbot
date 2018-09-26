import json

from flask import Flask
from flask import current_app as app

from rich_messages.facebook_rich_messages import FacebookRichMessages
from rich_messages.google_rich_messages import GoogleRichMessages
from rich_messages.fulfillment_payload import FulfillmentPayload


class City(object):
    """Handle the ask_cells_ask_cells_cidades responses"""

    def __init__(self):
        pass

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
        _google_rich = GoogleRichMessages()

        # query cells address by district
        query_address = {"city" : "guaiba",
                         "district": district.lower()}
        # do the query
        _cells_address = app.db.cells.find(query_address)

        # Iter cell address for facebook ang google payload
        _button_list_facebook = []
        _button_list_google = []
        for i, _address in enumerate(_cells_address):
            _button_list_facebook.append(dict(
                type="postback",
                title=_address["label"],
                payload=str(i+1),
            ))

            _button_list_google.append(dict(
                title=_address["label"],
                optionInfo=dict(key="escolho o numero %s" % str(i+1))
            ))            
            
        _list_title = "Os endereços das células em Guaíba, %s são: " % district

        # generate facebook rich list
        _facebook_message = _fb_rich.button_list(_list_title, _button_list_facebook)
        _google_message = _google_rich.button_list(_list_title, _button_list_google)

        _message = _fulfill.append('facebook', _facebook_message)
        _message = _fulfill.append('google', _google_message)

        return _message

    def eldorado(self, district):
        """Return Eldorado Cells by the given district"""

        return 'Ask Eldorado'
