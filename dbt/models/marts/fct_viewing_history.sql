with source as (
    select * from {{ ref('stg_viewing_history') }}
)

select
    {{ dbt_utils.generate_surrogate_key(['user_id', 'video_id', 'date_watched']) }} as view_sk,
    user_id,
    video_id,
    date_watched,
    watch_time,
    created_at
from source
