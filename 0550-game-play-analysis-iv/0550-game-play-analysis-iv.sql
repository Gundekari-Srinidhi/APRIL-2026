SELECT ROUND(
    COUNT(DISTINCT a.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity),
    2
) AS fraction
FROM Activity a
JOIN Activity b
ON a.player_id = b.player_id
WHERE b.event_date = (
    SELECT MIN(event_date)
    FROM Activity
    WHERE player_id = a.player_id
)
AND DATEDIFF(a.event_date, b.event_date) = 1;