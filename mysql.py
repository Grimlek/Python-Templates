#!/usr/bin/env python

import pymysql
import csv

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='database')

cursor = conn.cursor()
cursor.execute("SELECT columns FROM table_name")

names = []
for row in cursor:
    names.append(row[0])

#
# May need a file to import/export data into/from the database
#
with open("file_path_tab_delimited.txt") as f:
    reader = csv.reader(f, delimiter="\t") # tab delimited reader
    list = list(reader) # convert file to list, quick solution


cursor.execute("query")
print(cursor._executed) # print query executed

conn.commit() # commit update/delete/insert/etc.... queries
cursor.close()
conn.close()
