import os
import unittest
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import constants
import pandas as pd

class TestDBConnection(unittest.TestCase):
    def setUp(self):
        DATABASE_URL = os.getenv("DATABASE_URL").replace("postgres://", "postgresql://")
        self.engine = create_engine(DATABASE_URL)

    def tearDown(self):
        self.engine.dispose()

    def test_db_connection(self):
        try:
            connection = self.engine.connect()
            self.assertTrue(connection is not None)
        except OperationalError:
            self.fail("Could not establish a connection to the database")

    def test_sp500_table(self):
        try:
            connection = self.engine.connect()
            result = pd.read_sql_query(f"SELECT * FROM {constants.SP500_TABLE}", connection)
            self.assertTrue(result is not None)
        except OperationalError:
            self.fail("Could not establish a connection to the database")

    def test_stockpred_table(self):
        try:
            connection = self.engine.connect()
            result = pd.read_sql_query(f"SELECT * FROM {constants.STOCKPRED_TABLE}", connection)
            self.assertTrue(result is not None)
        except OperationalError:
            self.fail("Could not establish a connection to the database")

if __name__ == '__main__':
    unittest.main()