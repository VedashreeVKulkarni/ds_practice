# Write your MySQL query statement below
SELECT p.product_name , s.price,s.year 
FROM sales s
JOIN product p 
ON p.product_id=s.product_id