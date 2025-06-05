-- models/staging/stg_viewing_history.sql

with source as (
    select * from {{ source('raw', 'viewing_history') }}
)

select
    user_id::int,
    video_id::int,
    watch_time::int,
    date_watched::date
from source
