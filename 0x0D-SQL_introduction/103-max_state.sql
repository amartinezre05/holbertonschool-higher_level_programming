-- displays the max temperature of each state (ordered by State name).

SELECT 'state', MAX(value) as temp FROM temperatures
GROUP by state
RDER by state;
