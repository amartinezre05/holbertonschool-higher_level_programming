-- displays the max temperature of each state (ordered by State name).

SELECT 'state', MAX(value) as max_temp
FROM temperatures
GROUP by state
ORDER by state;
