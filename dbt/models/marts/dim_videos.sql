with source as (
    select * from {{ ref('stg_videos') }}
)

select
    video_id,
    title,
    lower(genre) as genre,
    duration,
    release_year
from source
