#!/usr/bin/python3
""" lists all states with a name """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s\
                ORDER BY id", (argv[4], ))
    states = cur.fetchall()
    for row in states:
        print(row)
    cur.close()
    db.close()
