#!/usr/bin/python3
"""script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """db connection"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    """interact cursor with database"""
    cur = db.cursor()
    """execute query"""
    cur.execute("""SELECT * FROM states WHERE name
            LIKE BINARY '%{}%' ORDER BY id""".format(argv[4]))
    """fetch rows as list"""
    states = cur.fetchall()
    for state in states:
        print(state)
    """close cursor and database"""
    cur.close()
    db.close()
