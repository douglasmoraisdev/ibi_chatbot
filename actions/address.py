import json

from flask import Flask

from rich_messages.facebook_rich_messages import FacebookRichMessages
from rich_messages.google_rich_messages import GoogleRichMessages
from rich_messages.fulfillment_payload import FulfillmentPayload
import config.logconfig

app = Flask(__name__)


class Address(object):
    """Handle the ask_cells_ask_cells_cidades responses"""

    def __init__(self):
        with open('json_db/json_db.json') as _json_db:
            self.db = json.loads(_json_db.read())

    def generate_image_url_google_maps(self, complete_address):
        """Return a Google Maps static image"""

        _base_gm_url = "https://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=16&scale=1&size=600x600&maptype=roadmap&key=AIzaSyBUf4hCdRA6HSmsvpjYSpJZOFOZ5ClThy0&format=png&visual_refresh=true&markers=size:mid|color:0xff0000|label:|%s"

        _image_url = _base_gm_url % (complete_address.replace(' ','+'), complete_address.replace(' ','+'))

        return _image_url

    def generate_url_google_maps(self, complete_address, zip_code):
        """Return a Google Maps Url Address"""        

        _base_gm_url = "https://maps.google.com/?q=%s,%s"

        _google_url = _base_gm_url % (complete_address, zip_code)

        return _google_url.replace(' ', '+')


    def google_maps_from_address(self, params, outputContexts):
        """Return google maps image_url and url from a give address"""

        _google_maps_info=dict()

        # response object
        _fulfill = FulfillmentPayload()

        # objects for rich responses
        _fb_rich = FacebookRichMessages()        
        
        address_index = params['number'][0]
        district_name = outputContexts[0]['parameters']['ibi_districts'].lower()

        # query for the address info
        _address_info = self.db.get('cells').get('cities')\
            .get('guaiba').get('districts')\
            .get(district_name)[int(float(address_index))-1]

        # get the google maps static image url
        _google_maps_img_url = self.generate_image_url_google_maps(
                                    _address_info["complete_address"]
                                )

        # get the google maps url
        _google_maps_url = self.generate_url_google_maps(
                                    _address_info["complete_address"],
                                    _address_info["cep"],
                            )

        # format the output for facebook
        _google_maps_info["image_url"] = _google_maps_img_url
        _google_maps_info["url"] = _google_maps_url
        _facebook_message = _fb_rich.address_link(_google_maps_img_url, 
                                                  _google_maps_url, 
                                                  _address_info["complete_address"],
                                                  )

        _message = _fulfill.append('facebook', _facebook_message)

        app.logger.info('_google_maps_info %s' % _message)

        return _message
