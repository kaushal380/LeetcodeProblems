--difficulty: easy


-- Write your MySQL query statement below
select id from weather w1 where temperature > (select temperature from weather w2 where w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY))



-- DATE_SUB(w1.recordDate, INTERVAL 1 DAY)
--DATEDIFF(w1.recordDate, w2.recordDate) = 1
-- DATEADD(day, 1, W2.recordDate)
-- DATE_ADD(W2.recordDate, INTERVAL 1 DAY)


-- Select the IDs from Weather where the temperature is higher than the previous day
-- SELECT w1.id
-- FROM Weather w1, Weather w2
-- WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1
--   AND w1.temperature > w2.temperature;
