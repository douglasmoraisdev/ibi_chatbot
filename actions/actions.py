from .cidades import Cidades


class Actions(object):

    def ac_hello(self, request):

        return 'Hello response'

    def ask_celulas_ask_celulas_cidades(self, params):

        _action_class = Cidades()

        if ('ibi_cidade' in params) and ('ibi_bairros' in params):
            _cidade = params['ibi_cidades'].lower()
            _bairro = params['ibi_bairros'].lower()

            return getattr(_action_class, _cidade)(_bairro)
        else:
            return getattr(_action_class, 'guaiba')('centro')
