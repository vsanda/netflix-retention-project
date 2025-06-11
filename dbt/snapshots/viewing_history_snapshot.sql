{% snapshot viewing_history_snapshot %}
{{
    config(
        target_schema = 'snapshots',
        unique_key = "user_id || '-' || video_id || '-' || cast(date_watched as text)",
        strategy = 'timestamp',
        updated_at = 'created_at',
        invalidate_hard_deletes = True
    )
}}

select
  user_id,
  video_id,
  watch_time,
  date_watched,
  created_at
from {{ ref('stg_viewing_history') }}

{% endsnapshot %}
