SELECT w.id, wp.age, w.coins_needed, w.power
FROM Wands w
JOIN Wands_Property wp 
ON w.code = wp.code
WHERE wp.is_evil = 0 AND w.coins_needed = (
    SELECT MIN(w2.coins_needed) FROM Wands w2 WHERE w2.code = w.code AND w2.power = w.power
)
ORDER BY w.power DESC, wp.age DESC;