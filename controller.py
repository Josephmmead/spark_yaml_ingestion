from pyspark.sql import SparkSession
import yaml
from get_schemas import get_schema


def controller(config_location, config_name):
    spark = SparkSession.builder.getOrCreate()
    yaml_path = config_location + config_name

    with open(yaml_path, 'r') as f:
        contents = yaml.safe_load(f)

    for input in contents['inputs']:
        csv_metadata = contents['inputs'][input]
        location = csv_metadata['location']
        schema = get_schema()[csv_metadata['schema']]
        table_name = csv_metadata['dataframe']
        file_type = csv_metadata['type']

        df = spark.read.csv(location, schema=schema)
        df.createOrReplaceTempView(table_name)

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
    
    for output in contents['outputs']:
        output_df = spark.table(output['output_df'])
        file_format = output['target_file_format']
        output_location = output['output_location']

        output_df.write.format(file_format).mode('overwrite').save(output_location, header=True)

    spark.stop()

if __name__ == "__main__":
    config_location = ".\\yamls\\"
    config_name = "customer_demo.yml"
    # config_name = "customer.yml"
    controller(config_location, config_name)
