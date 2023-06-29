import unittest
from unittest.mock import patch
from pyspark.sql import SparkSession
from controller import controller
from get_schemas import get_schema

config_location = "./tests/test_resources/"
config_name = 'test_yaml.yaml'

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.spark = SparkSession.builder.getOrCreate()

    def tearDown(self):
        self.spark.stop()

    def test_controller_inputs(self):

        controller(config_location, config_name)

        # Assert that the temporary table has been created
        self.assertTrue(self.spark.catalog._jcatalog.tableExists('customer'))

    def test_controller_inputs_unhappy_path(self):

        controller(config_location, config_name)

        # Assert that the temporary table has been created
        self.assertFalse(self.spark.catalog._jcatalog.tableExists('test'))

    def test_process_sql(self):
        # Capture the output of `print` statements
        with patch('builtins.print') as mock_print:
            controller(config_location, config_name)

        # Assert that the print statements were called with the expected messages
        mock_print.assert_called_with('Creating temp view: sql1')


if __name__ == '__main__':
    unittest.main()
