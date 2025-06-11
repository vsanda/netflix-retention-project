with snapshot as (
    select * from {{ ref('users_snapshot') }}
),

final as (
    select
        {{ dbt_utils.generate_surrogate_key(['user_id', 'dbt_valid_from']) }} as user_sk,
        user_id,
        signup_date,
        country,
        device_type,
        plan_type,
        dbt_valid_from as valid_from,
        dbt_valid_to as valid_to,
        case
            when dbt_valid_to is null then true
            else false
        end as is_current
    from snapshot
)

select * from final
