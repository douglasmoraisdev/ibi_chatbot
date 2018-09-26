import unittest
import json

from flask import Flask
from flask_pymongo import PyMongo

from actions.city import City
import config.dbconfig as dbconfig


class CityUnitTests(unittest.TestCase):
    """Unit test City Class"""

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["MONGO_URI"] = dbconfig.MONGO_URI
        mongo = PyMongo(self.app)
        self.app.db = mongo.db

    def test_barra(self):
        """Test a ask about barra cells"""

        with self.app.app_context():
            _cidade = City()
            _resp = _cidade.barra('Centro')

            self.assertIn("fulfillmentMessages", _resp)

    def test_guaiba(self):
        """Test a ask about guaiba cells"""

        with self.app.app_context():
            _cidade = City()
            _resp = _cidade.guaiba('Jardim dos Lagos')

            self.assertIn("Os endereços das células em Guaíba", str(_resp))
            self.assertIn("Jardim", str(_resp))
            self.assertIn("facebook", str(_resp))
            self.assertIn("google", str(_resp))
            self.assertIn("Maica", str(_resp))


if __name__ == '__main__':
    unittest.main()
