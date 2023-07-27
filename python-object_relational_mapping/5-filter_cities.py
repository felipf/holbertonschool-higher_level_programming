#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all cities of that state"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """database connection"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    """cursor creation"""
    cur = db.cursor()
    """query execution"""
    cur.execute("""SELECT cities.name FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name LIKE BINARY %s""", (argv[4],))
    """fetch rows as list"""
    cities = cur.fetchall()
    """lista vacia para agregar ciudades a la lista(si, lo puse en español srry)"""
    citiesNames = []
    for city in cities:
        citiesNames.append(city[0])
    """add comma with a space"""
    cityList = ", ".join(citiesNames)
    print(cityList)
    """close cursor and database"""
    cur.close()
    db.close()
