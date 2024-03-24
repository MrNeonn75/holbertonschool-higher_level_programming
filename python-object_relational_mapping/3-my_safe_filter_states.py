#!/usr/bin/python3

"""
Once again, write a script that takes in arguments
and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that
is safe from MySQL injections!
"""

from sys import argv
import MySQLdb
    
if __name__ == "__main__":
    server = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = server.cursor()
    cursor.execute("""SELECT * FROM `states`""")

    [print(state) for state in cursor.fetchall() if state[1] == argv[4]]

    cursor.close()
    server.close()
