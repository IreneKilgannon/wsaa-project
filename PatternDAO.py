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
        attkeys=['patternID', 'brand','category', 'fabric_type', 'description', 'ownerID']
        pattern = {}
        currentkey = 0
        for attrib in resultLine:
            pattern[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return pattern

# View all patterns
    def getAll(self):
        cursor = self.getCursor()
        sql = "SELECT * from patterns"
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
        sql = "SELECT * FROM patterns WHERE patternID = %s"
        values = (patternID, )
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue 

# View by Category
    def findByCategory(self, category):
        cursor = self.getCursor()
        sql = "SELECT * FROM patterns WHERE category = %s"
        values = (category, )
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue 

# View by Brand
    def findByBrand(self, brand):
        cursor = self.getCursor()
        sql = "SELECT * FROM patterns WHERE brand = %s"
        values = (brand, )
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue 

# View by Fabric Type
    def findByBrand(self, fabric_type):
        cursor = self.getCursor()
        sql = "SELECT * FROM patterns WHERE fabric_type = %s"
        values = (fabric_type, )
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue 

# View by Owner Name
    def findByOwner(self, name):
        cursor = self.getCursor()
        sql = "SELECT p.*, u.name FROM patterns p join users u on p.ownerID = u.usersID WHERE u.name = %s"
        values = (name, )
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue 
    
# Create a pattern
    def create(self, pattern):
        cursor = self.getCursor()
        sql = "INSERT INTO patterns (patternID, brand, category, fabric_type, description, ownerID) VALUES (%s, %s, %s, %s, %s, %s)"
        values = [pattern['patternID'], pattern['brand'], pattern['category'], pattern['fabric_type'], pattern['description'], pattern['ownerID']]
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    
# Update a pattern
    def update(self, patternID, pattern):
        cursor = self.getCursor()
        sql = "UPDATE patterns SET brand = %s, category = %s, fabric_type = %s, description = %s, ownerID= %s where patternID = %s"
        values = (pattern.get("brand"), pattern.get("category"), pattern.get("fabric_type"), pattern.get("description"), patternID)
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