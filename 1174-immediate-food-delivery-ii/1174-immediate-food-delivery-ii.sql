# Write your MySQL query statement below



select ROUND((count(case when datediff(order_date,customer_pref_delivery_date) = 0 then 1 end)/(select count(distinct customer_id) from Delivery))*100,2) as immediate_percentage from Delivery WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date)
    FROM Delivery
    GROUP BY customer_id
);;