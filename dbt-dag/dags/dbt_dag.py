import os
from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping
from pathlib import Path

dbt_project_path = Path("/usr/local/airflow/dags/dbt_snow_data_pipeline")

prifile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id = "snowflake_conn",
        profile_args={"database": "dbt_db", "schema": "dbt_schema"}
    )
)

dbt_snowfake_dag = DbtDag(
    project_config=ProjectConfig(dbt_project_path),
    operator_args={"install_deps": True},
    profile_config=prifile_config,
    execution_config=ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt"),
        start_date=datetime(2024, 1, 1),
        schedule_interval="@daily",
        catchup=False,
        dag_id="dbt_dag"
)