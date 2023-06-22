from pyspark.sql import SparkSession
import yaml
from get_schemas import get_schema


def controller(config_location, config_name):
    spark = SparkSession.builder.getOrCreate()
    yaml_path = config_location + config_name

    with open(yaml_path, 'r') as f:
        contents = yaml.safe_load(f)

    process_inputs(contents, spark)
    process_sql(contents, spark)

    spark.stop()


def process_inputs(contents, spark):
    for input in contents['inputs']:
        csv_metadata = contents['inputs'][input]
        location = csv_metadata['location']
        schema = get_schema()[csv_metadata['schema']]
        table_name = csv_metadata['dataframe']
        file_type = csv_metadata['type']

        df = spark.read.csv(location, schema=schema)
        df.createOrReplaceTempView(table_name)


def process_sql(contents, spark):
    for sql_command in contents['sql_statements']:
        command_name = sql_command['name']
        query = sql_command['query']
        temp_table = sql_command['temp_table']
        drop_tables = sql_command['drop_temp_views']

        if temp_table:
            print(f'Creating temp view: {command_name}')
            spark.sql(query).createOrReplaceTempView(command_name)
        else:
            print(f'Executing SQL statement: {command_name}')
            result_df = spark.sql(query)
            result_df.show()

        if len(drop_tables) >= 1:
            for table in drop_tables:
                print(f'Dropping temp view: {table}')
                spark.catalog.dropTempView(table)
    

if __name__ == "__main__":
    config_location = ".\\spark_yaml_ingestion\\yamls\\"
    config_name = "customer_demo.yml"
    # config_name = "customer.yml"
    controller(config_location, config_name)
