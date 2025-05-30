select 
    orders.order_key,
    orders.customer_key,
    orders.status_code,
    orders.total_price,
    orders.order_date,
    order_items_summary.gross_item_sales_amount,
    order_items_summary.item_discount_amount
from {{ ref('stg_tpch_orders') }} as orders
join {{ ref('int_order_item_summary') }} as order_items_summary
    on orders.order_key = order_items_summary.order_key
order by
    orders.order_date