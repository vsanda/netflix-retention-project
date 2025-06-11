-- models/staging/churn_labels.sql
with source as (
    select * from {{ source('raw', 'churn_labels') }}
)

select
    user_id::int,
    churned::boolean,
    churn_date::date,
    created_at::timestamp
from source

