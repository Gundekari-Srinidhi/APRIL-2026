# Write your MySQL query statement below

SELECT customer_id,count(customer_id) as count_no_trans FROM Visits v LEFT JOIN Transactions t on t.visit_id = v.visit_id WHERE t.visit_id IS NULL GROUP BY v.customer_id;