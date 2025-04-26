## 1 - Creating virtual environment
* Create virtual environment - 
    `python -m venv myenv`
* Activate virtual environment - 
    `source myenv/bin/activate`
* Deactivate virtual environment - 
    `deactivate

## 2 - dbt setup
* Install dbt-snowflake
    `pip install dbt-snowflake`
* Install dbt-core
    `pip install dbt-core`
* Initialize dbt - 
    `dbt init`
* provide project name - 
    `dbt_snow_data_pipeline`
* provide value - https://<this_value>.snowflakecomputing.com
* dev username
* password
* dev role - dbt_role
* warehouse - dbt_wh
* database - dbt_db
* schema - dbt_schema
* threads (1 or more) - 10
    
## 3 - Configure `dbt_project.yml`
* created to models folder
    - staging
    - marts

## 4 - Create `packages.yml` useful for surrogate key
* added `dbt-labs/dbt_utils`
* install this package `dbt deps`

## 5 - Run model in dbt
* `dbt run` or `dbt run -s <model_name>` or `dbt run --select <model_name>`

## 6 - Create source and staging table
* source - 
    snowflake_sample_data.tpch_sf1.orders
    snowflake_sample_data.tpch_sf1.lineitem
* staging tables - 
    dbt_db.dbt_schema.stg_tpch_orders
    dbt_db.dbt_schema.stg_tpch_line_item

## 7 - Transformed model
* fact tables and data marts
    dbt_db.dbt_schema.int_order_item
    dbt_db.dbt_schema.int_order_item_summary
    dbt_db.dbt_schema.fct_orders

## 8 - Macro functions
* Created macro function - 
    discounted_amount

## 9 - Generic and Singular tests
* Generic tests
    model/marts/generic_tests.yml
* Singular tests
    tests/fct_orders_discount.sql
    tests/fct_orders_date_valid.sql

## 10 - Deploy model using airflow
* install astro - `curl -sSL install.astronomer.io | sudo bash -s`
* make directory - `mkdir dbt-dag` -> `cd dbt-dag`
* `astro dev init`
* Edit docker and requirements.txt file
* `astro dev start`



