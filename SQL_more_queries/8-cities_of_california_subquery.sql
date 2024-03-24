-- Lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id, cities.name FROM hbtn_0d_usa.cities, hbtn_0d_usa.states
    WHERE hbtn_0d_usa.cities(state_id) = hbtn_0d_usa.state(id)
    AND hbtn_0d_usa.states(name) = "California"
    ORDER BY hbtn_0d_usa.cities(id);