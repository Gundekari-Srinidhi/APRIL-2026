# Write your MySQL query statement below

SELECT name,bonus FROM Employee e LEFT JOIN Bonus b on e.empId = b.empId WHERE b.bonus < 1000 or b.empId is null; 