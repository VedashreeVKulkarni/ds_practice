# Write your MySQL query statement below
SELECT w.id
from Weather w
JOIN Weather t
 ON Datediff(w.recordDate,t.recordDate)=1
WHERE w.temperature>t.temperature



