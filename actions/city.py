import json


class City(object):
    """Handle the ask_cells_ask_cells_cidades responses"""

    def __init__(self):
        with open('json_db/json_db.json') as _json_db:
            self._db = json.loads(_json_db.read())

    def barra(self, district):
        return 'Ask Barra'

    def guaiba(self, district):
        _cells_address = self._db.get('cells').get('cities')\
                           .get('guaiba').get('districts')\
                           .get('jardim dos lagos')

        _address_str = "O endereço das células em Guaíba, %s são: " % district
        _address_list = ""
        for _address in _cells_address:
            _address_list = "%s, \n%s" % (_address_list, _address)

        _address_str = "%s %s" % (_address_str, _address_list)

        return _address_str

    def eldorado(self, district):

        return 'Ask Eldorado'
