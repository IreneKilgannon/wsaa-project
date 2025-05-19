import mysql.connector
import config as cfg

# Python script that connects to MySQL and creates the sewing_patterns database

# Connect to mysql
mydb = mysql.connector.connect(
    host= cfg.mysql['host'],
    user= cfg.mysql['user'],
    password= cfg.mysql['password'],
    database= cfg.mysql['database'],
    )

# Create database
my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE sewing_patterns")

# Confirm the creation of the sewing_patterns database
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)














