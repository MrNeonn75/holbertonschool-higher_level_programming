#!/usr/bin/python3

"""
Once again, write a script that takes in arguments
and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that
is safe from MySQL injections!
"""

import sys
import MySQLdb


def main():
   """ Main function """
    
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    
    cur = conn.cursor()
    search = sys.argv[4]
    cur.execute("SELECT * FROM `states`", (search,))
    row = cur.fetchall()
    
    [print(state) for state in cur.fetchall() if state[1] == argv[4]]
        
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
