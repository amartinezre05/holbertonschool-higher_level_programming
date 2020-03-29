#!/usr/bin/python3
""" lists all cities with a name """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    sql_query = "SELECT cities.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id"
    cur.execute(sql_query, (argv[4], ))
    states = cur.fetchall()
    line = ''
    num = len(states)
    for row in states:
        if num > 1:
            line += row[0] + ', '
        else:
            line += row[0]
        num -= 1
    print(line)
    cur.close()
    db.close()
