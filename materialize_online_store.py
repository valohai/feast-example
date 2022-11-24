from datetime import datetime
from feast import FeatureStore

store = FeatureStore(repo_path="./feast_repository")
store.materialize_incremental(end_date=datetime.now())