import unittest
from unittest.mock import patch
from pyspark.sql import SparkSession
from controller import controller, process_inputs, process_sql
from get_schemas import get_schema

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.spark = SparkSession.builder.getOrCreate()

    def tearDown(self):
        self.spark.stop()

    def test_process_inputs(self):
        contents = {
            'inputs': {
                'customer': {
                    'location': '.\data\customer.csv',
                    'schema': 'customer_schema',
                    'dataframe': 'customer',
                    'type': 'type1'
                }
            }
        }

        process_inputs(contents, self.spark)

        # Assert that the temporary table has been created
        self.assertTrue(self.spark.catalog._jcatalog.tableExists('customer'))

    def test_process_sql(self):
        contents = {
            'sql_statements': [
                {
                    'name': 'sql1',
                    'query': 'SELECT * FROM table1',
                    'temp_table': True,
                    'drop_temp_views': []
                }
            ]
        }

        # Create a temporary view for testing
        self.spark.createDataFrame([(1, 'John'), (2, 'Jane')], ['id', 'name']).createOrReplaceTempView('table1')

        # Capture the output of `print` statements
        with patch('builtins.print') as mock_print:
            process_sql(contents, self.spark)

        # Assert that the print statements were called with the expected messages
        mock_print.assert_called_with('Creating temp view: sql1')


if __name__ == '__main__':
    unittest.main()
