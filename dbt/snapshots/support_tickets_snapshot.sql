{% snapshot support_tickets_snapshot %}
{{
  config(
    target_schema='snapshots',
    unique_key='ticket_id',
    strategy='timestamp',
    updated_at='updated_at',
    invalidate_hard_deletes=True
  )
}}

select
  ticket_id,
  user_id,
  issue_type,
  ticket_date,
  resolved,
  created_at,
  updated_at
from {{ ref('stg_support_tickets') }}

{% endsnapshot %}
