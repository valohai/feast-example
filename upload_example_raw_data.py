import os
import click
import psycopg2

from feast.file_utils import replace_str_in_file
from feast.infra.utils.postgres.connection_utils import df_to_postgres_table
from feast.infra.utils.postgres.postgres_config import PostgreSQLConfig
from datetime import datetime, timedelta
from feast.driver_test_data import create_driver_hourly_stats_df

end_date = datetime.now().replace(microsecond=0, second=0, minute=0)
start_date = end_date - timedelta(days=15)

driver_entities = [1001, 1002, 1003, 1004, 1005]
driver_df = create_driver_hourly_stats_df(driver_entities, start_date, end_date)

postgres_host = os.environ("FEAST_POSTGRES_HOSTNAME")
postgres_port = "5432"
postgres_database = "postgres"
postgres_schema = "public"
postgres_user = os.environ("FEAST_POSTGRES_USERNAME")
postgres_password = os.environ("FEAST_POSTGRES_PASSWORD")

db_connection = psycopg2.connect(
    dbname=postgres_database,
    host=postgres_host,
    port=int(postgres_port),
    user=postgres_user,
    password=postgres_password,
    options=f"-c search_path={postgres_schema}",
)

with db_connection as conn, conn.cursor() as cur:
    cur.execute('DROP TABLE IF EXISTS "feast_driver_hourly_stats"')

df_to_postgres_table(
    config=PostgreSQLConfig(
        host=postgres_host,
        port=int(postgres_port),
        database=postgres_database,
        db_schema=postgres_schema,
        user=postgres_user,
        password=postgres_password,
    ),
    df=driver_df,
    table_name="feast_driver_hourly_stats",
)

