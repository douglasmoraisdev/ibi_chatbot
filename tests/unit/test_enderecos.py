import unittest
import json

from flask import Flask
from flask_pymongo import PyMongo

from actions.city import City
from actions.actions import Actions
import config.dbconfig as dbconfig


class EnderecosTests(unittest.TestCase):
    """Unit test City Class"""

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["MONGO_URI"] = dbconfig.MONGO_URI
        mongo = PyMongo(self.app)
        self.app.db = mongo.db

    def test_endereco_guaiba_jardim(self):
        """Test a ask to a guaiba, jardim address"""

        with self.app.app_context():
            _action = Actions()
            _resp = _action.ask_cells_cities_select_address(
                        dict(number='1.0'),
                            [dict(parameters=dict(ibi_districts='jardim dos lagos'))],
                            dict(title='Rua Cenair Maica, 440'),
                    )

            self.assertIn("image_url", str(_resp))
            self.assertIn("maps.googleapis.com", str(_resp))
            self.assertIn("maps.google.com", str(_resp))
            self.assertIn("Rua+Cenair+Maica,+440", str(_resp))



if __name__ == '__main__':
    unittest.main()
