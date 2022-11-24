# feast-example
Example integration of Feast feature store with Valohai MLOps platform.

This example assumes PostgresSQL backend for Feast, but can be modified to work with any backend(s).


# What is a feature store?

ML models don't like raw data, but refined data. Data scientists call the refined data *features*. 

A feature store defines:

* What features are available
* Where is the the raw data stored
* How features are transformed from the raw data
* Where the refined features data will be stored

Feature store offers ability to:
* Pull training data (slow, high latency)
* Pull inference data (fast, low latency)

# What is Feast?

**While feature stores are commonly services, Feast is really not.**

Feast is "just" a Python library (SDK).

With Feast SDK, you define features in Python and update them into your data store. 

You can also query the features back as a batch (offline / training) or single entity (online / deployment).

# What does this example do?

Valohai steps available:
* **initialize** - Uploads the example raw data into the SQL server
* **apply** - Update changed feature definitions into the store. Usually triggered by new commit in the code repository.
* **materialize** - Update precalculated data into the online store. Usually scheduled daily by CI/CD.
* **fetch (offline)** - Fetch a batch of historical features for training a model
* **fetch (online)** - Fetch features of single entity for model inference 



# Setup

1. Make sure you have a Postgres SQL server which is accessible from an Valohai execution.
2. Set these environment variables in your Valohai project:
- `FEAST_POSTGRES_HOSTNAME`
- `FEAST_POSTGRES_USERNAME`
- `FEAST_POSTGRES_PASSWORD`
3. Execute the `initialize` step in Valohai. It uploads the raw example data into a database table `feast_driver_hourly_stats`.
4. Execute the `apply` step in Valohai. It uploads all the feature definitions into the database.
