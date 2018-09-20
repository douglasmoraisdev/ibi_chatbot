from app import app
import unittest
import json


class CidadesCelulasTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        _json_data = open('tests/request_celula_barra.json').read()
        self.barra_payload = json.loads(_json_data)

        _json_data = open('tests/request_celula_guaiba_bairros.json').read()
        self.guaiba_payload = json.loads(_json_data)

    def test_post_barra(self):

        _payload = self.barra_payload

        result = self.app.post('/', data=json.dumps(_payload),
                               content_type='application/json')

        self.assertEqual(result.status_code, 200)

    def test_post_guaiba_bairros(self):

        _payload = self.guaiba_payload

        result = self.app.post('/', data=json.dumps(_payload),
                               content_type='application/json')

        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()
