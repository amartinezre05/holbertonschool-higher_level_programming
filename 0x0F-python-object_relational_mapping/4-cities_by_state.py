#!/usr/bin/python3
""" lists all cities with a name """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    sql_query = "SELECT cities.id, cities.name, states.name\
                FROM cities JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id"
    cur.execute(sql_query)
    states = cur.fetchall()
    for row in states:
        print(row)
    cur.close()
    db.close()
