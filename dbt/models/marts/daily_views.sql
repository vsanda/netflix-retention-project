select
    date_watched,
    count(distinct user_id) as unique_viewers,
    count(*) as total_views,
    sum(watch_time) as total_watch_time
from {{ ref('stg_viewing_history') }}
group by date_watched
order by date_watched
