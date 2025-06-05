with user_views as (
    select
        user_id,
        count(distinct date_watched) as active_days,
        count(*) as total_views,
        sum(watch_time) as total_watch_time
    from {{ ref('stg_viewing_history') }}
    group by user_id
),

user_subscriptions as (
    select
        user_id,
        max(plan_type) as current_plan,
        max(is_active::int) as is_active_subscriber
    from {{ ref('stg_subscriptions') }}
    group by user_id
)

select
    u.user_id,
    u.signup_date,
    u.country,
    u.device_type,
    us.current_plan,
    us.is_active_subscriber,
    uv.active_days,
    uv.total_views,
    uv.total_watch_time
from {{ ref('stg_users') }} u
left join user_views uv on u.user_id = uv.user_id
left join user_subscriptions us on u.user_id = us.user_id
