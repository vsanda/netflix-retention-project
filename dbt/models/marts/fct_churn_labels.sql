with snapshot as (
    select * from {{ ref('churn_labels_snapshot') }}
),

final as (
    select
        {{ dbt_utils.generate_surrogate_key(['user_id', 'dbt_valid_from']) }} as churn_sk,
        user_id,
        churned,
        churn_date,
        dbt_valid_from as valid_from,
        dbt_valid_to as valid_to,
        created_at
    from snapshot
)

select * from final
