-- models/staging/stg_videos.sql
with source as (
    select * from {{ source('raw', 'videos') }}
)   

select
    video_id::int,
    title,
    genre,
    duration::int,
    release_year::int
from source