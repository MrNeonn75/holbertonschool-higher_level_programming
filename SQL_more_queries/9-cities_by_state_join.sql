-- Lists all cities contained in the database hbtn_0d_usa.
SELECT id, name FROM cities WHERE id IN (
    SELECT id FROM states
) ORDER BY id;
SELECT name FROM states WHERE id IN (
    SELECT state_id FROM cities
) ORDER BY cities.id;