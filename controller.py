from pyspark.sql import SparkSession
import yaml
from schemas.get_schemas import get_schema



def controller(config_location,config_name):
    spark = get_spark()

    with open(config_location+config_name, 'r') as f:
        contents = yaml.safe_load(f)

    for input in contents['inputs']:
        csv_metadata = contents['inputs'][input] 
        location = csv_metadata['location']
        schema = get_schema()[csv_metadata['schema']]
        table_name = csv_metadata['dataframe']
        file_type = csv_metadata['type']

        print(f"location: {location}, table_name: {table_name}, file_type: {file_type}")
        df = spark.read.csv(location, schema=schema)
        df.show()
        df.createOrReplaceTempView(table_name)
        
        

    for sql_command in contents['sql_statements']:
        command_name = sql_command['name']
        query = sql_command['query']
        temp_table = sql_command['temp_table']

        result_df = spark.sql(query)
        if temp_table:
            result_df.createOrReplaceTempView(command_name)

        result_df.show()

    stop_spark(spark)


def get_spark():
    return SparkSession.builder.getOrCreate()

def stop_spark(spark):
    spark.stop()



if __name__ == "__main__":
    config_location = "C:\\Users\\joseph.mead\\Dev\\spark_injection_project\\yamls\\"
    config_name = "customer.yml"
    controller(config_location,config_name)

