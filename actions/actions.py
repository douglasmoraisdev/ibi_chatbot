from flask import Flask

from .city import City
from .address import Address
import config.logconfig

app = Flask(__name__)

class Actions(object):
    """Handle the intents resposes by action names """

    def ask_cells_cities(self, params, outputContexts):
        """Return the list of Cell addresses by city and district"""

        _action_class = City()

        if ('ibi_cities' in params) and ('ibi_districts' in params):
            _city = params['ibi_cities'].lower()
            _district = params['ibi_districts']

            return getattr(_action_class, _city)(_district)
        else:
            return getattr(_action_class, 'guaiba')('centro')

    def ask_cells_cities_select_address(self, params, outputContexts):
        """Return the map link for the selected address"""

        _address = Address()

        app.logger.info('params %s' % params)
        app.logger.info('outputContexts %s' % outputContexts)

        _address_info = _address.google_maps_from_address(params, outputContexts)

        return _address_info
    