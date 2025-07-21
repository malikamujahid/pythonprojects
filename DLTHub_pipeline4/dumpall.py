import dlt
from order_unnest import unnest_order
from customer_unnest import unnest_customers
from items_unnest import unnest_items
from stores_unnest import unnest_store
from employee_unnest import unnest_employees


pipeline = dlt.pipeline(
    pipeline_name="postgres_to_snowflake_multi",
    destination="snowflake",
    dataset_name="unnested_data" 
)


load_info = pipeline.run([
    unnest_order(),
    unnest_customers(),
    unnest_items(),
    unnest_store(),
    unnest_employees()
])

print(load_info)
