import json


class Cidades(object):

    def __init__(self):
        _json_db = open('json_db/json_db.json').read()
        self._db = json.loads(_json_db)

    def barra(self, bairro):
        return 'Ask Barra'

    def guaiba(self, bairro):
        _enderecos_celulas = self._db.get('celulas').get('cidades')\
                           .get('guaiba').get('bairros')\
                           .get('jardim dos lagos')

        _enderecos_str = "O endereço das células em Guaíba, %s são: " % bairro
        _enderecos_list = ""
        for _enderecos in _enderecos_celulas:
            _enderecos_list = "%s, \n%s" % (_enderecos_list, _enderecos)

        _enderecos_str = "%s %s" % (_enderecos_str, _enderecos_list)

        return _enderecos_str

    def eldorado(self, bairro):

        return 'Ask Eldorado'
