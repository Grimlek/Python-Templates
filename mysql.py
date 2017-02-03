#!/usr/bin/env python

import pymysql
import csv

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='database')

cur = conn.cursor()
cur.execute("SELECT columns FROM table_nume")

names = []
for row in cur:
    names.append(row[0])

#
# Possibly need a file to import/export data into/from the database
#
with open("file_path_tab_delimited.txt") as f:
    reader = csv.reader(f, delimiter="\t") # tab delimited reader
    list = list(reader) # convert file to list, quick solution


cur.execute("query")
print(cur._executed) # print query executed

conn.commit() # commit update/delete/insert/etc.... queries
cur.close()
conn.close()