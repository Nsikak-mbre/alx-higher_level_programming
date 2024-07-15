#!/usr/bin/python3
"""
List values that start with 'N' from the database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cursor = db.cursor()
    query = """
    SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC
    """
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
