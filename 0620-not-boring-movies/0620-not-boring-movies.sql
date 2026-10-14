# Write your MySQL query statement below
SELECT id,movie,description,rating 
FROM Cinema
WHERE Mod(id,2) AND description !='boring'
ORDER BY rating DESC;
