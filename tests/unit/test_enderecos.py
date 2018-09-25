import unittest
import json
from actions.city import City
from actions.actions import Actions


class EnderecosTests(unittest.TestCase):
    """Unit test City Class"""

    def setUp(self):
        pass

    def test_endereco_guaiba_jardim(self):
        """Test a ask to a guaiba, jardim address"""

        _action = Actions()
        _resp = _action.ask_cells_cities_select_address(
                    dict(number='1.0'),
                         [dict(parameters=dict(ibi_districts='jardim dos lagos'))]
                )

        self.assertIn("image_url", str(_resp))
        self.assertIn("maps.googleapis.com", str(_resp))
        self.assertIn("maps.google.com", str(_resp))
        self.assertIn("Rua+Cenair+Maica,+440", str(_resp))



if __name__ == '__main__':
    unittest.main()
