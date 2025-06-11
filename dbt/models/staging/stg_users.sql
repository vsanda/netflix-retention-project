-- models/staging/stg_users.sql
with source as (
    select * from {{ source('raw', 'users') }}
)

select
    user_id::int,
    signup_date::date,
    country,
    lower(device_type) as device_type,
    lower(plan_type) as plan_type,
    created_at::timestamp,
    updated_at::timestamp
from source

