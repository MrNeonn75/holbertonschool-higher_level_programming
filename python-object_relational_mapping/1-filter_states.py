#!/usr/bin/python3

"""
Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

def main():
    # The variables for getting data.
    username = sys.argv[0]
    password = sys.argv[1]
    database = sys.argv[2]
    
    # Connect to MySQL server
    server = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = username,
        passwd = password,
        db = database
    )
    
    # Cursor
    cursor = server.cursor()
    
    # Query
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id"
    
    # Send request
    cursor.execute(query)
    
    # Get result
    result = cursor.fetchall()
    
    # Print result
    for data in result:
        print(data)
    
    # Close connection
    cursor.close()
    server.close()
    
if (__name__ == "__main__"):
    main()
    