import mysql.connector
import config as cfg

class PatternDAO:
    host =""
    user = ""
    password =""
    database =""
    connection = ""
    cursor =""


    def __init__(self):
        self.host= cfg.mysql['host']
        self.user= cfg.mysql['user']
        self.password= cfg.mysql['password']
        self.database= cfg.mysql['database']

    # Setting up connectors to database
    def getCursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
#
    def convertToDictionary(self, resultLine):
        attkeys=['userID', 'firstname', 'surname', 'email']
        user = {}
        currentkey = 0
        for attrib in resultLine:
            user[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return user

# View all patterns
    def getAll(self):
        cursor = self.getCursor()
        sql = "SELECT * from users"
        cursor.execute(sql)
        results = cursor.fetchall()
        patterns = []
        for row in results:
            patterns.append(self.convertToDictionary(row))
        self.closeAll()
        return results

# View by ID
    def findByID(self, patternID):
        cursor = self.getCursor()
        sql = "SELECT * FROM patterns WHERE userID = %s"
        values = (patternID, )
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue 

    
# Create a user
    def create(self, user):
        cursor = self.getCursor()
        sql = "INSERT INTO users (userID, name, email) VALUES (%s, %s, %s)"
        values = [user['userID'], user['first_name'], user['surname'], user['email']]
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    
# Update a user
    def update(self, pattern):
        cursor = self.getCursor()
        sql = "UPDATE users SET first_ = %s, category = %s, fabric_type = %s, description = %s, owne
        values = (pattern.get("brand"), pattern.get("category"), pattern.get("fabric_type"), pattern.g
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return pattern

# Delete
    def delete(self, patternID):
        cursor = self.getCursor()
        sql = "DELETE FROM patterns WHERE patternID = %s"
        values = (patternID, )
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        print("Pattern deleted")


# DO LATER. GET Basics working first.

# Send email to Borrow a pattern


# Send email to Request return of a pattern


patternDAO = PatternDAO()