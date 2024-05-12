/*1st Task*/
/*i)*/
SELECT COUNT(lon) AS stigmas, date(t)
FROM positions
GROUP BY date(t)
ORDER BY COUNT(lon);
/*ii)*/
SELECT type, COUNT(id) AS greek_ships
FROM vessels
where flag = 'Greece'
GROUP BY type
ORDER BY type;
/*iii)*/
with shipcount(ship_type, total) as (
	select type, count(distinct(vessel_id))
	from positions, vessels, vesseltypes
	where speed > 30 and vessel_id = vessels.id and type = code
	group by type
	)
select distinct(vessel_id), type, description, total as total_of_ships_by_type
from positions, vessels, vesseltypes, shipcount
where speed > 30 and vessel_id = vessels.id and type = code and code = ship_type;
/*iv)*/
SELECT date(t), COUNT(lon) AS stigmas
FROM positions, vessels, vesseltypes
WHERE (date(t) BETWEEN '2019-08-14' and '2019-08-18') 
AND (vessel_id = vessels.id AND type = code AND description LIKE 'Passenger%')
GROUP BY date(t)
ORDER BY date(t);
/*v)*/
WITH question1(answer1) AS (
	SELECT Distinct(vessel_id)
	FROM positions, vessels, vesseltypes
	WHERE (date(t) BETWEEN '2019-08-15' and '2019-08-18') 
	AND (vessel_id = vessels.id AND type = code AND description LIKE 'Cargo%')
	),
totalspeeds(ships, distance) AS (
	SELECT vessel_id, SUM(speed)
	FROM positions
	WHERE (date(t) BETWEEN '2019-08-12' AND '2019-08-19')
	GROUP BY vessel_id
	),
question2(answer2) AS (
	SELECT DISTINCT(vessel_id)
	FROM positions, vessels, vesseltypes, totalspeeds
	WHERE vessel_id = ships AND distance = 0
	AND (vessel_id = vessels.id AND type = code AND description LIKE 'Cargo%')
	)
SELECT answer1 as stopped_once, answer2 as remained_stoped
FROM question1, question2;

/*2nd Task*/
ALTER SYSTEM SET shared_buffers TO '256MB';

/*3rd Task*/
SET max_parallel_workers_per_gather = 1024;

/*4th Task*/
/*ii)*/
CREATE INDEX index2 ON vessels USING HASH(flag);
/*iii)*/
CREATE INDEX index3 ON positions USING BTREE(speed ASC);
/*iv)*/
CREATE INDEX index4 ON positions USING BTREE(date(t));
/*i)*/
CREATE INDEX index4 ON positions USING BTREE(date(t));