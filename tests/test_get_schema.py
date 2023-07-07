import unittest
import get_schemas as get_schemas


class TestGetSchema(unittest.TestCase):

    TESTNAME = "TestGetSchema"

    # This test shows that you return a pyspark schema when you pass the schema to the get_schema function
    # I have passed this as a str for easier testing
    def test_get_schema_happy_path(self):
        schema = 'customer_schema'
        expected = "StructType([StructField('customer', StringType(), False), StructField('customer_id', StringType(), False)])"
        self.assertEquals(str(get_schemas.get_schema()[schema]), expected)
    
    # This test shows that a key error is raised when the schema that is given does not exist in the dictionary created by the get_schema function
    def test_get_schema_unhappy_path(self):
        schema = 'fake_schema'
        expected = None
        with self.assertRaises(KeyError):
            get_schemas.get_schema()[schema]


if __name__ == '__main__':
    unittest.main()



