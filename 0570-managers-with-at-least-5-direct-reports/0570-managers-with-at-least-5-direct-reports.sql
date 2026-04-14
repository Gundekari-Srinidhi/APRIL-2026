# Write your MySQL query statement below


SELECT e.name from employee e join employee i on e.id = i.managerId group by e.id,e.name HAVING count(i.id)>=5;