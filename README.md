# DataEngineering-
### This folder contains my Data Engineering concepts projects 

# Automated ETL Process with Apache Airflow in EC2 and AWS S3
### This project automates the Extract, Tranform, Load (ETL) process using Apache Airflow on an Amazon EC2 instance. The ETL process extracts data from various sources, transforms it, and loads the transformed data into an Amazon S3 bucket.

## Prerequisites 
#### Amazon EC2 instance with  Apache Airflow installed and configured.
#### AWS credentials with permissions to access Amazon S3.

## Install Dependencies:
#### Make sure to install any necessary dependencies for your data extraction and transformation scripts.

### Configure AWS Credentials:

#### Ensure that AWS credentials are configured on your EC2 instance to allow access to Amazon S3. You can do this by setting environment variables or using AWS CLI configuration.

### Configure Apache Airflow:

#### Apache Airflow should already be installed and configured on your EC2 instance. Make sure that the necessary connections and variables are set up in the Airflow UI for accessing AWS S3 and any other required services.

### Update DAG Configuration:

#### Update the twitter_dag.py DAG configuration file in the dags/ directory according to your ETL workflow requirements. Specify the tasks for data extraction, transformation, and loading, along with their dependencies and scheduling parameters.

### Run Apache Airflow:

#### Start the Apache Airflow scheduler and webserver on your EC2 instance using the appropriate commands. Make sure that Airflow is up and running without any errors.

### Monitor and Trigger Workflow:

#### Access the Apache Airflow web interface in your browser and navigate to the DAGs page. You should see the etl_twitter DAG listed. Monitor the DAG runs and trigger manual executions as needed.

