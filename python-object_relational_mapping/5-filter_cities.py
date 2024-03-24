#!/usr/bin/python3

"""
Takes in the name of a state as an argument
and lists all cities of that state, using the
database hbtn_0e_4_usa
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
    
   state_name = sys.argv[4]
   cur = conn.cursor()
   cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s ORDER BY cities.id", (state_name,))
   row = cur.fetchall()
   re = ""
    
   print(", ".join([c[2] for c in cur.fetchall() if c[4] == argv[4]]))
        
   print(re[0:-2:])
    
   cur.close()
   conn.close()


if __name__ == "__main__":
   main()
