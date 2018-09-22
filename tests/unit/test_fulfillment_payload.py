import unittest
import json
from rich_messages.facebook_rich_messages import FacebookRichMessages
from rich_messages.fulfillment_payload import FulfillmentPayload


class FulfillmentPayloadUnitTests(unittest.TestCase):
    """Unit test City Class"""

    def setUp(self):
        pass

    def test_append_payload(self):
        """Test payload append"""

        _fb_rich = FacebookRichMessages()
        _fulfill = FulfillmentPayload()

        _title = "Algum Titulo"
        _button_list = []

        _button_list.append(dict(type="postback",
                                 title="1 - Rua Abacate, 123 bl P",
                                 postback="1"))
        _button_list.append(dict(type="postback",
                                 title="2 - Av. Maça, 99 fundos",
                                 postback="2"))

        _button_message = _fb_rich.button_list(_title, _button_list)

        _complete_message = _fulfill.append('facebook', _button_message)

        self.assertIn("payload", str(_complete_message))
        self.assertIn("facebook", str(_complete_message))
        self.assertIn("template_type", str(_complete_message))
        self.assertIn("Titulo", str(_complete_message))
        self.assertIn("1 - Rua Abacate, 123 bl P", str(_complete_message))
        self.assertIn("2 - Av. Maça, 99 fundos", str(_complete_message))


if __name__ == '__main__':
    unittest.main()
