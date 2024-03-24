#!/usr/bin/python3

"""
Takes in the name of a state as an argument
and lists all cities of that state, using the
database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
   session = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
   cursor = session.cursor()
   cursor.execute("\
      SELECT * \
      FROM `cities` as `c` \
      INNER JOIN `states` as `s` \
      ON `c`.`state_id` = `s`.`id` \
      ORDER BY `c`.`id`\
   ")

   print(", ".join([c[2] for i in cursor.fetchall() if i[4] == sys.argv[4]]))

   cursor.close()
   session.close()

