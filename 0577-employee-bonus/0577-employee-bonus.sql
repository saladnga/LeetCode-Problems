# Write your MySQL query statement below
SELECT a.name, b.bonus
FROM Employee a LEFT JOIN Bonus b ON a.empID = b.empID
WHERE b.bonus < 1000 OR b.bonus IS NULL