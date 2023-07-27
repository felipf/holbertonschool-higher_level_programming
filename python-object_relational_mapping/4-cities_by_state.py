#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """db connection"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    """interact cursor with database"""
    cur = db.cursor()
    """execute query"""
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                JOIN states ON cities.state_id = states.id ORDER BY id;""")
    """fetch rows as list"""
    states = cur.fetchall()
    for state in states:
        print(state)
    """close cursor and database"""
    cur.close()
    db.close()
