-- models/staging/stg_support_tickets.sql

with source as (
    select * from {{ source('raw', 'support_tickets') }}
)

select
    user_id::int,
    issue_type,
    ticket_date::date,
    resolved::boolean
from source
