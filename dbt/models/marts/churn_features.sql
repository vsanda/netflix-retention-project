select
    u.user_id,
    u.signup_date,
    c.churned,
    c.churn_date,
    us.is_active,
    count(st.ticket_date) as num_support_tickets
from {{ ref('stg_users') }} u
left join {{ ref('stg_churn_labels') }} c on u.user_id = c.user_id
left join {{ ref('stg_subscriptions') }} us on u.user_id = us.user_id
left join {{ ref('stg_support_tickets') }} st on u.user_id = st.user_id
group by u.user_id, u.signup_date, c.churned, c.churn_date, us.is_active
