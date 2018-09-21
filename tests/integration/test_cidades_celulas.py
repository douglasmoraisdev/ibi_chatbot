from app import app
import unittest
import json


class CityCellsIntegrationTest(unittest.TestCase):
    """
    Test integration in ask Cells location dialogs
    """

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        with open('tests/request_celula_barra.json') as _json_data:
            self.barra_payload = json.loads(_json_data.read())

        with open('tests/request_celula_guaiba_bairros.json') as _json_data:
            self.guaiba_payload = json.loads(_json_data.read())

    def test_post_barra(self):
        """Test a ask about barra cells"""

        _payload = self.barra_payload

        result = self.app.post('/', data=json.dumps(_payload),
                               content_type='application/json')

        self.assertEqual(result.status_code, 200)
        self.assertIn('richResponse', str(result.data))

    def test_post_guaiba_bairros(self):
        """Test a ask about guaiba cells"""

        _payload = self.guaiba_payload

        result = self.app.post('/', data=json.dumps(_payload),
                               content_type='application/json')

        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()
