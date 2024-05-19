# Description: This file contains the unit tests for the database connection and the existence of the tables in the database.
import os
import unittest
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import constants
import pandas as pd

class TestDBConnection(unittest.TestCase):

    #set up the test
    def setUp(self):
        DATABASE_URL = os.getenv("DATABASE_URL").replace("postgres://", "postgresql://")
        self.engine = create_engine(DATABASE_URL)

    #tear down the test
    def tearDown(self):
        self.engine.dispose()

    #test the database connection
    def test_db_connection(self):
        try:
            connection = self.engine.connect()
            self.assertTrue(connection is not None)
        except OperationalError:
            self.fail("Could not establish a connection to the database")

    #test the existence of the stockpred table
    def test_stockpred_table(self):
        try:
            connection = self.engine.connect()
            result = pd.read_sql_query(f"SELECT * FROM {constants.STOCKPRED_TABLE}", connection)
            self.assertTrue(result is not None)
        except OperationalError:
            self.fail("Could not establish a connection to the database")


    #test the existence of the stockprice table
    def test_stockprice_table(self):
        try:
            connection = self.engine.connect()
            result = pd.read_sql_query(f"SELECT * FROM {constants.STOCKPRICE_TABLE}", connection)
            self.assertTrue(result is not None)
        except OperationalError:
            self.fail("Could not establish a connection to the database")

#run the tests
if __name__ == '__main__':
    unittest.main()