#!/usr/bin/python3
"""print all states from database where name matches the argument safely."""
import MySQLdb
import sys


def main(argv):
    """Guards content."""
    if len(argv) != 5:
        return ()
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%(name)s", {'name': argv[4]})
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    main(sys.argv)
