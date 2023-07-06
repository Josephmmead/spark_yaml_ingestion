# Spark YAML Ingestion

This project demonstrates how to ingest data into Spark using a YAML configuration file. It reads CSV files, applies schemas, and executes SQL statements based on the provided configuration.

## Prerequisites

- Python 3.7 or above
- PySpark 

## Installation

1. Clone the repository:

   git clone https://github.com/Josephmmead/spark_yaml_ingestion

2. cd spark-yaml-ingestion

3. pip install -r requirements.txt

## Usage

1. Ensure that your CSV and YAML configuration files are in the appropriate directory.

2. Modify the following variables to specify the location of your YAML configuration file:

    config_location = ".\\spark_yaml_ingestion\\yamls\\"
    config_name = "customer_demo.yml"

4. Save the changes and exit the text editor.

5. Run the controller.py script to start the data ingestion process.

6. Monitor the console output for progress updates and SQL statement results.

7. Once the process is complete, the temporary views created during the execution will be automatically dropped.

## Configuration

The YAML configuration file (customer_demo.yml in this example) should be structured as follows:

``` yaml
inputs:
  input1:
    location: path/to/input1.csv
    schema: schema1
    dataframe: table1
    type: csv
  input2:
    location: path/to/input2.csv
    schema: schema2
    dataframe: table2
    type: csv

sql_statements:
  - name: sql_statement1
    query: SELECT * FROM table1 WHERE column1 = 'value'
    temp_table: true
    drop_temp_views: ['table1']

  - name: sql_statement2
    query: SELECT column1, AVG(column2) AS average FROM table2 GROUP BY column1
    temp_table: false
    drop_temp_views: []

outputs:

  - name: sample_output
    output_df: final_df
    target_file_format: csv
    output_location: .\output
```

The inputs section specifies the CSV files to be ingested. Each input should have a unique name and provide the following details:

- location: The path to the CSV file.
- schema: The name of the schema for the CSV file, defined in the get_schema() function.
- dataframe: The name of the DataFrame to be created from the CSV data.
- type: The type of the input file (e.g., CSV, JSON).

The sql_statements section contains the SQL statements to be executed. Each statement should include the following information:

- name: A descriptive name for the SQL statement that is also used as the temp view name.
- query: The SQL query to be executed.
- temp_table: A boolean value indicating whether to create a temporary view for the query.
- drop_temp_views: A list of temporary view names to be dropped after executing the query.

The outputs section specifies the variables need to output the data from your sql queries into a file:

- name: A descriptive name for the specific output.
- output_df: The name of the DataFrame that you are wanting to have written out.
- target_file_format: Specifices the file type that you are wanting for your output file (ie csv, parquet, json, ect).
- output_location: The location of where the written file will be written to.

Feel free to modify the configuration file according to your specific data ingestion requirements.
