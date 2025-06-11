{% snapshot users_snapshot %}
{{
  config(
    target_schema='snapshots',
    unique_key='user_id',
    strategy='timestamp',
    updated_at='updated_at',
    invalidate_hard_deletes=True
  )
}}

select * from {{ ref('stg_users') }}

{% endsnapshot %}
