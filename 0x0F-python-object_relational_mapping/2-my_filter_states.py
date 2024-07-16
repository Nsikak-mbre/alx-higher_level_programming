#!/usr/bin/python3
"""
display values in table that matches specified argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    state_name = sys.argv[4]
    with MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306) as db:
        with db.cursor() as cursor:
            query = """
            SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC
            """.format(state_name)
            cursor.execute(query)
            states = cursor.fetchall()
            for state in states:
                print(state)
