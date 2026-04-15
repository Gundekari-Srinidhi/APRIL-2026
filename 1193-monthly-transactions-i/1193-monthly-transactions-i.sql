# Write your MySQL query statement below


SELECT  DATE_FORMAT(trans_date,'%Y-%m') as month,country,count(*) as trans_count,sum(case when state = "approved" then 1 else 0 end) as approved_count,sum(amount) as trans_total_amount,SUM(CASE WHEN state = "approved" THEN amount ELSE 0 END) AS approved_total_amount FROM Transactions  group by DATE_FORMAT(trans_date,'%Y-%m'),country;