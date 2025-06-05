with first_week_views as (
    select
        u.user_id,
        count(*) as views_in_first_week
    from {{ ref('stg_users') }} u
    join {{ ref('stg_viewing_history') }} vh on u.user_id = vh.user_id
    where vh.date_watched between u.signup_date and u.signup_date + interval '7 day'
    group by u.user_id
)

select
    user_id,
    views_in_first_week,
    case when views_in_first_week > 10 then true else false end as is_binge_watcher
from first_week_views
