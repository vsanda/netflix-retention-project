--  models/staging/stg_subscriptions.sql

with source as (
    select * from {{ source('raw', 'subscriptions') }}
)

select
    user_id::int,
    plan_type,
    start_date::date,
    end_date::date,
    is_active::boolean
from source
