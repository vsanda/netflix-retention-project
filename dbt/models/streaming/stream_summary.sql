-- models/streaming/stream_summary.sql

{{ config(materialized='table') }}

with sessionized as (
  select
    user_id,
    content_id,
    min(timestamp) as session_start,
    max(timestamp) as session_end,
    count(*) as total_events,
    count(*) filter (where event_type = 'pause') as pause_count,
    count(*) filter (where event_type = 'seek') as seek_count,
    count(*) filter (where event_type = 'device_change') as device_change_count
  from {{ source('public', 'streaming_logs') }}
  group by user_id, content_id
)

select *,
  extract(epoch from (session_end - session_start)) as session_duration_sec
from sessionized
