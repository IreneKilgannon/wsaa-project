import mysql.connector
import config as cfg

# Python script that connects to MySQL and creates the users and patterns tables for the sewing_patterns database.

# Connect to mysql
mydb = mysql.connector.connect(
    host= cfg.mysql['host'],
    user= cfg.mysql['user'],
    password= cfg.mysql['password'],
    database= cfg.mysql['database'],
    )


# Create users table
create_users_table = """
    CREATE TABLE users (
        userID INTEGER AUTO_INCREMENT,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        email VARCHAR(320) NOT NULL,
        password_hash VARCHAR (255),
        PRIMARY KEY (userID)
        );
    """

my_cursor = mydb.cursor()
my_cursor.execute(create_users_table)
print("Users table created. ")


# Create patterns table
create_patterns_table = """
    CREATE TABLE patterns (
        patternID VARCHAR(100),
        brand VARCHAR(100) NOT NULL,
        category  ENUM ('Coat', 'Coordinates', 'Dress', 'Jacket', 'Shirt', 'Skirt', 'Sleepwear', 'Trousers', 'Top') NOT NULL,
        fabric_type ENUM ('Woven', 'Stretch', 'All') NOT NULL,
        description VARCHAR(255),
        format ENUM ('Paper', 'PDF'),
        userID INTEGER NOT NULL,
        PRIMARY KEY (patternID),
        FOREIGN KEY (userID) REFERENCES users (userID)
    );
    """

my_cursor.execute(create_patterns_table)
print("Patterns table created.")