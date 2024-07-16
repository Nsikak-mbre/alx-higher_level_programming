#!/usr/bin/python3
"""
List all cities from database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    with MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306) as db:
        with db.cursor() as cursor:
            query = ("SELECT cities.id, cities,name, state.name"
                     "FROM cities "
                     "JOIN states ON cities.state_id = state.id "
                     "ORDER BY cities.id ASC")
            cursor.execute(query)
            cities = cursor.fetchall()
            for city in cities:
                print(city)
