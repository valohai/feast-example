from datetime import datetime
import pandas as pd
from feast import FeatureStore

store = FeatureStore(repo_path="./feast_repository")
entity_rows = [
    {
        "driver_id": 1001,
        "val_to_add": 1000,
        "val_to_add_2": 2000,
    },
    {
        "driver_id": 1002,
        "val_to_add": 1001,
        "val_to_add_2": 2002,
    },
]

features_to_fetch = [
    "driver_hourly_stats:acc_rate",
    "transformed_conv_rate:conv_rate_plus_val1",
    "transformed_conv_rate:conv_rate_plus_val2",
]
returned_features = store.get_online_features(
    features=features_to_fetch,
    entity_rows=entity_rows,
).to_dict()

for key, value in sorted(returned_features.items()):
    print(key, " : ", value)