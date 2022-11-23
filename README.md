# feast-example
Example integration of Feast feature store with Valohai MLOps platform.

This example assumes PostgresSQL backend for Feast, but can be modified to work with any backend.

# PostgresSQL connection:
Make sure you have a PostgresSQL server which is accessible from an Valohai execution.

To let Feast SDK/CLI access the database, set these environment variables in your Valohai project:
- FEAST_POSTGRES_HOSTNAME
- FEAST_POSTGRES_USERNAME
- FEAST_POSTGRES_PASSWORD

