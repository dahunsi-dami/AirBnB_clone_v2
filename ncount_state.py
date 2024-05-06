#!/usr/bin/python3
""""""

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="HBNB_MYSQL_USER",
        passwd="HBNB_MYSQL_PWD",
        db="HBNB_MYSQL_DB",
        charset="utf8"
    )

    curr = conn.cursor()
    curr.execute(f"""SELECT COUNT(*) FROM states""")
    rows = curr.fetchall()

    for row_2 in rows:
        for row_3 in row_2:
            print(row_3)

    curr.close()
    conn.close()
