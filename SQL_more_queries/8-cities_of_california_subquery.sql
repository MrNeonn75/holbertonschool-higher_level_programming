-- Lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id, cities.name FROM hbtn_0d_usa.cities, hbtn_0d_usa.states
    WHERE cities.state_id = state.id
    AND states.name = "California"
    ORDER BY cities.id;