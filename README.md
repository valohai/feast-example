# feast-example
Example integration of Feast feature store with Valohai MLOps platform.

This example assumes PostgresSQL backend for Feast, but can be modified to work with any backend(s).

# Postgres
Make sure you have a Postgres SQL server which is accessible from an Valohai execution.

Set these environment variables in your Valohai project:
- FEAST_POSTGRES_HOSTNAME
- FEAST_POSTGRES_USERNAME
- FEAST_POSTGRES_PASSWORD

