{% snapshot churn_labels_snapshot %}
{{
  config(
    target_schema='snapshots',
    unique_key='user_id',
    strategy='timestamp',
    updated_at='created_at',
    invalidate_hard_deletes=True
  )
}}

select * from {{ ref('stg_churn_labels') }}

{% endsnapshot %}
