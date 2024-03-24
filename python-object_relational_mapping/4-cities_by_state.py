#!/usr/bin/python3

"""
A script that lists all cities
from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
   db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
   cursor = db.cursor()
   cursor.execute("\
      SELECT `c`.`id`, `c`.`name`, `s`.`name` \
      FROM `cities` as `c` \
      INNER JOIN `states` as `s` \
      ON `c`.`state_id` = `s`.`id` \
      ORDER BY `c`.`id`\
   ")

   [print(i) for i in cursor.fetchall()]

   cursor.close()
   db.close()
