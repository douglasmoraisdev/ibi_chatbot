from .city import City


class Actions(object):
    """Handle the intents resposes by action names """

    def ac_hello(self, request):

        return 'Hello response'

    def ask_cells_cities(self, params):

        _action_class = City()

        if ('ibi_cities' in params) and ('ibi_districts' in params):
            _city = params['ibi_cities'].lower()
            _district = params['ibi_districts']

            return getattr(_action_class, _city)(_district)
        else:
            return getattr(_action_class, 'guaiba')('centro')

    def ask_cells_cities_select_address(self, params):

        _action_class = City()

        if ('ibi_cities' in params) and ('ibi_districts' in params):
            _city = params['ibi_cities'].lower()
            _district = params['ibi_districts']

            return getattr(_action_class, _city)(_district)
        else:
            return getattr(_action_class, 'guaiba')('centro')

    def ask_cells_cities_show_route(self, params):

        _action_class = City()

        if ('ibi_cities' in params) and ('ibi_districts' in params):
            _city = params['ibi_cities'].lower()
            _district = params['ibi_districts']

            return getattr(_action_class, _city)(_district)
        else:
            return getattr(_action_class, 'guaiba')('centro')
