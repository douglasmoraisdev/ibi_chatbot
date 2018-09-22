import unittest
import json
from actions.city import City


class CityUnitTests(unittest.TestCase):
    """Unit test City Class"""

    def setUp(self):
        with open('tests/request_celula_barra.json') as _json_data:
            self.barra_payload = json.loads(_json_data.read())

        with open('tests/request_celula_guaiba_bairros.json') as _json_data:
            self.guaiba_payload = json.loads(_json_data.read())

    def test_barra(self):
        """Test a ask about barra cells"""

        _cidade = City()
        _resp = _cidade.barra('Centro')

        self.assertIn("fulfillmentMessages", _resp)

    def test_guaiba(self):
        """Test a ask about guaiba cells"""

        _cidade = City()
        _resp = _cidade.guaiba('Centro')

        self.assertIn("O endereço das células em Guaíba", str(_resp))
        self.assertIn("Centro", str(_resp))


if __name__ == '__main__':
    unittest.main()
