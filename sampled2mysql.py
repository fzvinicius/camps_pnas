
#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

'''
    This script was not used (too slow). We used bulk insert from mysql in the following way:

    $ mysql -u root -p instagram_nov2014 --local-infile=1
    mysql> set autocommit=0; set unique_checks=0; set foreign_key_checks=0;
    mysql> load data local infile '/disco/2/quake/selfies/pnas/sampled_16M_users.txt' into table collect_users (resource_id);
    mysql> commit;
    $mysqldump -u root - instagram_nov2014 > collect_users_16M.sql

'''

from mysql.connector.errors import Error
from mysql.connector import errorcode
import mysql.connector
import app


mysqlConnection = mysql.connector.connect(user=app.dbUser, password=app.dbPassword, host=app.dbHost, database=app.dbName)
cursor = mysqlConnection.cursor()
cursor.execute("SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci")


data = open("sampled_16M_users", "r")

for i, line in enumerate(data):
    uid = line.strip()
    query = "INSERT INTO collect_users (resource_id) VALUES (%s)"%uid
    cursor.execute(query)
    if (i % 10000 == 0): 
        mysqlConnection.commit()
        print i

cursor.close()

