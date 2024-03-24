#!/usr/bin/python3

"""
Lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

def main():
    # Variables for getting arguments
    username = sys.argv[0]
    password = sys.argv[1]
    database_name = sys.argv[2]
    
    # Connect to MySQL server
    server = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = username,
        passwd = password,
        db = database_name,
        charset = "utf8"
    )
    
    # A variable which we can use for working with server
    cursor = server.cursor()
    
    # A variable which we save request query
    query = "SELECT * FROM states ORDER BY states.id"
    
    # Execute MySQL command
    cursor.execute(query)
    
    # Get all rows
    results = cursor.fetchall()
    
    # Display the result 
    for data in results:
        print(data)
        
    # Close connection
    cursor.close()
    server.close()

if (__name__ == "__main__"):
    main()
