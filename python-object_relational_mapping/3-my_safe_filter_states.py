#!/usr/bin/python3
"""
List all states from a database sql query
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    search = argv[4]

    username = MySQLdb.escape_string(username)
    password = MySQLdb.escape_string(password)
    database = MySQLdb.escape_string(database)
    search = MySQLdb.escape_string(search)

    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database, charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name = {} ORDER BY id ASC".format(search))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
