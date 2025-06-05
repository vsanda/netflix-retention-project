with ticket_counts as (
    select
        user_id,
        count(*) as total_support_tickets
    from {{ ref('stg_support_tickets') }}
    group by user_id
)

select
    u.user_id,
    c.churned,
    c.churn_date,
    coalesce(tc.total_support_tickets, 0) as total_support_tickets
from {{ ref('stg_users') }} u
left join {{ ref('stg_churn_labels') }} c on u.user_id = c.user_id
left join ticket_counts tc on u.user_id = tc.user_id
