from pyspark.sql.types import StructField, StringType, StructType, IntegerType, DecimalType

def get_schema():
    schema_dict = {}

    customer_schema = StructType([StructField('customer', StringType(), False),
                                  StructField('customer_id', StringType(), False)])
    
    transaction_schema = StructType([StructField('customer_id', StringType(), False),
                                     StructField('transaction_id', IntegerType(), False),
                                     StructField('transaction_amount', DecimalType(18,2), False)])
    
    demographic_schema = StructType([StructField('customer', StringType(), False),
                                      StructField('customer_id', StringType(), False),
                                      StructField('gender', StringType(), True),
                                      StructField('age', IntegerType(), True),
                                      StructField('country', StringType(), False),
                                      StructField('state', StringType(), False),
                                      StructField('salary', DecimalType(), False)])
    schema_dict['customer_schema'] = customer_schema
    schema_dict['transaction_schema'] = transaction_schema
    schema_dict['demographic_schema'] = demographic_schema

    return schema_dict

