with user_activity as (
    select
        u.user_id,
        u.signup_date,
        vh.date_watched
    from {{ ref('stg_users') }} u
    left join {{ ref('stg_viewing_history') }} vh on u.user_id = vh.user_id
),

retention_flags as (
    select
        user_id,
        signup_date,
        bool_or(date_watched between signup_date and signup_date + interval '7 day') as retained_7d,
        bool_or(date_watched between signup_date and signup_date + interval '30 day') as retained_30d
    from user_activity
    group by user_id, signup_date
)

select
    user_id,
    signup_date,
    retained_7d,
    retained_30d
from retention_flags
