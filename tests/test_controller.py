import unittest
from unittest.mock import patch
from pyspark.sql import SparkSession
from controller import controller
import os

config_location = "./tests/test_resources/"
config_name = 'test_yaml.yaml'

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.spark = SparkSession.builder.getOrCreate()

    def tearDown(self):
        self.spark.stop()

    def test_controller(self):
        output_path = './tests/test_resources/output/'
        
        
        with patch('builtins.print') as mock_print:
            controller(config_location, config_name)

        # Assert that the temporary table has been created
        self.assertTrue(self.spark.catalog._jcatalog.tableExists('customer'))

        # Assert that the print statements were called with the expected messages
        mock_print.assert_called_with('Creating temp view: sql1')

        output_list = os.listdir(output_path)
        self.assertGreaterEqual(len(output_list), 1)

        for file in output_list:
            os.remove(output_path+file)


        


if __name__ == '__main__':
    unittest.main()
