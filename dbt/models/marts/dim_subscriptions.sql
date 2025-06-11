with snapshot as (
    select * from {{ ref('subscriptions_snapshot') }}
),

final as (
    select
        {{ dbt_utils.generate_surrogate_key(['user_id', 'dbt_valid_from']) }} as subscription_sk,
        user_id,
        plan_type,
        start_date,
        end_date,
        is_active,
        dbt_valid_from as valid_from,
        dbt_valid_to as valid_to,
        case
            when dbt_valid_to is null then true
            else false
        end as is_current
    from snapshot
)

select * from final
