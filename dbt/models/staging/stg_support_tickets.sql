-- models/staging/stg_support_tickets.sql

with source as (
    select * from {{ source('raw', 'support_tickets') }}
)

select
    ticket_id::int,
    user_id::int,
    lower(issue_type) as issue_type,
    ticket_date::date,
    resolved::boolean,
    created_at::timestamp,
    updated_at::timestamp
from source
