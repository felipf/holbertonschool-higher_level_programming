#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa: """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """db connection"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    """ interact cursor with database """
    cur = db.cursor()
    """execute query"""
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    """ fetch rows as list """
    states = cur.fetchall()

    for state in states:
        print(state)
    """close cursor and database"""
    cur.close()
    db.close()
