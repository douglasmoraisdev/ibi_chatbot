import unittest
import json
from rich_messages.facebook_rich_messages import FacebookRichMessages


class FbRichMsgUnitTests(unittest.TestCase):
    """Unit test City Class"""

    def setUp(self):
        with open('tests/request_celula_barra.json') as _json_data:
            self.barra_payload = json.loads(_json_data.read())

        with open('tests/request_celula_guaiba_bairros.json') as _json_data:
            self.guaiba_payload = json.loads(_json_data.read())

    def test_button_list(self):
        """Test a Facebook Button List message"""

        _fb_rich = FacebookRichMessages()

        _title = "Algum Titulo"
        _button_list = []

        _button_list.append(dict(type="postback",
                                 title="1 - Rua Abacate, 123 bl P",
                                 postback="1"))        
        _button_list.append(dict(type="postback",
                                 title="2 - Av. Maça, 99 fundos",
                                 postback="2"))

        _button_message = _fb_rich.button_list(_title, _button_list)

        self.assertIn("payload", str(_button_message))
        self.assertIn("facebook", str(_button_message))
        self.assertIn("template_type", str(_button_message))
        self.assertIn("Titulo", str(_button_message))
        self.assertIn("1 - Rua Abacate, 123 bl P", str(_button_message))
        self.assertIn("2 - Av. Maça, 99 fundos", str(_button_message))

if __name__ == '__main__':
    unittest.main()
