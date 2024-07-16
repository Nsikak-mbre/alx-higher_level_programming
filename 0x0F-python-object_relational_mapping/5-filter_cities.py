#!/usr/bin/python3
"""
takes a state as argument and list cities from that state
"""
import sys
import MySQLdb

if __name__ == '__main__':
    state_name = sys.argv[4]
    with MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306) as db:
        with db.cursor() as cursor:
            query = ("SELECT cities.id, cities.name "
                     "FROM cities "
                     "JOIN states ON cities.state_id = states.id "
                     "WHERE states.name = %s "
                     "ORDER BY cities.id ASC")
            cursor.execute(query, (state_name,))
            cities = cursor.fetchall()
            for city in cities:
                print(city)
