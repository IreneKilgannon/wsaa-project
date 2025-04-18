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
    def convertToDictionaryPatterns(self, resultLine):
        attkeys=['patternID', 'brand','category', 'fabric_type', 'description', 'format', 'userID']
        pattern = {}
        currentkey = 0
        for attrib in resultLine:
            pattern[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return pattern

    def convertToDictionaryUsers(self, resultLine):
        attkeys=['userID', 'first_name','last_name', 'email', 'password']
        user = {}
        currentkey = 0
        for attrib in resultLine:
            user[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return user

# View all patterns
    def getAll(self):
        cursor = self.getCursor()
        sql = "SELECT * from patterns"
        cursor.execute(sql)
        results = cursor.fetchall()
        patterns = []
        for row in results:
            patterns.append(self.convertToDictionaryPatterns(row))
        self.closeAll()
        return patterns

# View by ID
    def findByID(self, patternID):
        cursor = self.getCursor()
        sql = "SELECT * FROM patterns WHERE patternID = %s"
        values = (patternID, )
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionaryPatterns(result)
        self.closeAll()
        return returnvalue 

# View by Category
    def findByCategory(self, category):
        cursor = self.getCursor()
        sql = "SELECT * FROM patterns WHERE category = %s"
        values = (category, )
        cursor.execute(sql, values)
        result = cursor.fetchall()
        returnvalue = [self.convertToDictionaryPatterns(row) for row in result]
        self.closeAll()
        return returnvalue 

# View by Brand
    def findByBrand(self, brand):
        cursor = self.getCursor()
        sql = "SELECT * FROM patterns WHERE brand = %s"
        values = (brand, )
        cursor.execute(sql, values)
        result = cursor.fetchall()
        returnvalue = [self.convertToDictionaryPatterns(row) for row in result]
        self.closeAll()
        return returnvalue 

# View by Fabric Type
    def findByFabric(self, fabric_type):
        cursor = self.getCursor()
        sql = "SELECT * FROM patterns WHERE fabric_type = %s"
        values = (fabric_type, )
        cursor.execute(sql, values)
        result = cursor.fetchall()
        returnvalue = [self.convertToDictionaryPatterns(row) for row in result]
        self.closeAll()
        return returnvalue 

# View by UserID
    def findByUserID(self, userID):
        cursor = self.getCursor()
        sql = "SELECT * FROM patterns WHERE userID = %s"
        values = (userID, )
        cursor.execute(sql, values)
        result = cursor.fetchall()
        returnvalue = [self.convertToDictionaryPatterns(row) for row in result]
        self.closeAll()
        return returnvalue 
    
# Create a pattern
    def create(self, pattern):
        cursor = self.getCursor()
        sql = "INSERT INTO patterns (patternID, brand, category, fabric_type, description, format, userID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = [pattern['patternID'], pattern['brand'], pattern['category'], pattern['fabric_type'], pattern['description'], pattern['format'], pattern['userID']]
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    
# Update a pattern
    def update(self, pattern):
        cursor = self.getCursor()
        sql = "UPDATE patterns SET brand = %s, category = %s, fabric_type = %s, description = %s, format = %s, userID= %s WHERE patternID = %s"
        values = (pattern.get("brand"), pattern.get("category"), pattern.get("fabric_type"), pattern.get("description"), pattern.get('format'), pattern.get('userID'), pattern.get("patternID"))
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


###### User functions  LEAVING OUT password authentication for now. 
    def get_all_users(self):
        cursor = self.getCursor()
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        results = cursor.fetchall()
        users = []
        for row in results:
            users.append(self.convertToDictionaryUsers(row))
        self.closeAll()
        return users

    def create_user(self, user):
        cursor = self.getCursor()
        sql = "INSERT INTO users (userID, first_name, last_name, email) VALUES (%s, %s, %s, %s)"
        values = [user['userID'], user['first_name'], user['last_name'], user['email']]
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    
    def delete_user(self, userID):
        cursor = self.getCursor()
        sql = "DELETE FROM users WHERE userID = %s"
        values = (userID, )
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        print("User deleted")

    # Check user exists
    def user_exists(self, userID):
        for user in self.users:
            if user["userID"] == userID:
                return True
        return False

# Borrow a pattern
    def create_borrow_request(self, borrow):
        cursor = self.getCursor()
        sql = "INSERT INTO borrow_request (loadID, userID, patternID) VALUES (%s, %s, %s) "
        values = [borrow['loadID'], borrow['userID'], borrow['patternID']]
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid


# Send email to Request return of a pattern


patternDAO = PatternDAO()