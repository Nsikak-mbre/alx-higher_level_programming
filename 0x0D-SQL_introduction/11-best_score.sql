-- list all scores that meets certain criteria (conditional statemet)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;