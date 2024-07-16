#!/usr/bin/python3
"""
Displays values in table that matches specified arg, in a safe way
"""
import sys
import MySQLdb

if __name__ == '__main__':
    state_name = sys.argv[4]
    with MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306) as db:
        with db.cursor() as cursor:
            query = ("SELECT * FROM states WHERE BINARY name = %s "
                     "ORDER BY id ASC")
            cursor.execute(query, (state_name,))
            states = cursor.fetchall()
            for state in states:
                print(state)
