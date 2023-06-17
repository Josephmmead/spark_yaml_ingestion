from pyspark.sql.types import StructField, StringType, StructType, IntegerType, DecimalType

def get_schema():
    schema_dict = {}

    customer_schema = StructType([StructField('customer', StringType(), False),
                                  StructField('customer_id', StringType(), False)])
    
    transaction_schema = StructType([StructField('customer_id', StringType(), False),
                                     StructField('transaction_id', IntegerType(), False),
                                     StructField('transaction_amount', DecimalType(18,2), False)])
    
    schema_dict['customer_schema'] = customer_schema
    schema_dict['transaction_schema'] = transaction_schema

    return schema_dict

