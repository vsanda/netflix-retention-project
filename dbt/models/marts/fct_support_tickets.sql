with source as (
    select * from {{ ref('stg_support_tickets') }}
)

select
    {{ dbt_utils.generate_surrogate_key(['ticket_id']) }} as ticket_sk,
    ticket_id,
    user_id,
    issue_type,
    ticket_date,
    resolved,
    created_at,
    updated_at
from source
