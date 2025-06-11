{% snapshot subscriptions_snapshot %}
{{
  config(
    target_schema='snapshots',
    unique_key="user_id || '-' || cast(start_date as text)",
    strategy='timestamp',
    updated_at='updated_at',
    invalidate_hard_deletes=True
  )
}}

select * from {{ ref('stg_subscriptions') }}

{% endsnapshot %}
