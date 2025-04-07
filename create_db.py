import mysql.connector
import config as cfg

mydb = mysql.connector.connect(
    host= cfg.mysql['host'],
    user= cfg.mysql['user'],
    password= cfg.mysql['password'],
    database= cfg.mysql['database'],
    )

my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE sewing_patterns")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)