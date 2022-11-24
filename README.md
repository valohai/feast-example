# feast-example
Example integration of Feast feature store with Valohai MLOps platform.

This example assumes PostgresSQL backend for Feast, but can be modified to work with any backend(s).


# What is a feature store?

ML models don't like raw data, but refined data. Data scientists call the refined data *features*. Feature store is a service where you define features and how they are transformed from the raw data. You also define the source of the raw data and the storage for the refined data. In this example, they are both in the same Postgres database.

# What is Feast?

**Although feature stores are often services, Feast is really not.** It is just a Python library (SDK).

With Feast SDK, you define features in Python and update them into your designated data store. You can also query the features back as a batch (offline / training) or single (online / deployment).

# What does this example do?

There are four Valohai steps available:
* **initialize** - Uploads the example raw data into the SQL server
* **fetch (offline)** - Fetch historical features for training a model
* **fetch (online)** - Fetch features of single entity for model inference 
* **materialize** - Update precalculated data in the online store. Usually scheduled daily by CI/CD.
* **apply** - Update the data store after changing feature definitions. Usually triggered by new commit in the code repository.

# Setup

Make sure you have a Postgres SQL server which is accessible from an Valohai execution.

Set these environment variables in your Valohai project:
- `FEAST_POSTGRES_HOSTNAME`
- `FEAST_POSTGRES_USERNAME`
- `FEAST_POSTGRES_PASSWORD`

Finally execute the `initialize` step in Valohai. It uploads the raw example data into the database table `feast_driver_hourly_stats`.

You are now ready to run all the other steps.
