select * from {{ source('raw', 'support_tickets') }} limit 5
