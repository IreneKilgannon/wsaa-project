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
        try:
            cursor = self.getCursor()
            sql = "SELECT * from patterns"
            cursor.execute(sql)
            results = cursor.fetchall()

            if not results:
                return None
            
            patterns = []
            for row in results:
                patterns.append(self.convertToDictionaryPatterns(row))
            return patterns
        
        except Exception as e:
            print(f"Database error in getAll: {e}")
            raise
        finally:
            self.closeAll()

# View by ID
    def findByID(self, patternID):
        try:
            cursor = self.getCursor()
            sql = "SELECT * FROM patterns WHERE patternID = %s"
            values = (patternID, )
            cursor.execute(sql, values)
            result = cursor.fetchone()

            if not result:
                return None
            
            returnvalue = self.convertToDictionaryPatterns(result)
            return returnvalue
        
        except Exception as e:
            print(f"Database error in findByID: {e}")
            raise
        finally:
            self.closeAll()

# View by Category
    def findByCategory(self, category):
        try:
            cursor = self.getCursor()
            sql = "SELECT * FROM patterns WHERE category = %s"
            values = (category, )
            cursor.execute(sql, values)
            result = cursor.fetchall()

            if not result:
                return None
            
            returnvalue = self.convertToDictionaryPatterns(result)
            return returnvalue
        
        except Exception as e:
            print(f"Database error in findByCategory: {e}")
            raise
        finally:
            self.closeAll()

# View by Brand
    def findByBrand(self, brand):
        try:
            cursor = self.getCursor()
            sql = "SELECT * FROM patterns WHERE brand = %s"
            values = (brand, )
            cursor.execute(sql, values)
            result = cursor.fetchall()

            if not result:
                return None
            
            returnvalue = self.convertToDictionaryPatterns(result)
            return returnvalue
        
        except Exception as e:
            print(f"Database error in findByBrand: {e}")
            raise
        
        finally:
            self.closeAll()

# View by Fabric Type
    def findByFabric(self, fabric_type):
        try:
            cursor = self.getCursor()
            sql = "SELECT * FROM patterns WHERE fabric_type = %s"
            values = (fabric_type, )
            cursor.execute(sql, values)
            result = cursor.fetchall()

            if not result:
                return None
            
            returnvalue = self.convertToDictionaryPatterns(result)
            return returnvalue
        except Exception as e:
            print(f"Database error in findByFabric: {e}")
            raise
        finally:
            self.closeAll()

    # View by UserID
    def findByUserID(self, userID):
        try:
            cursor = self.getCursor()
            sql = "SELECT * FROM patterns WHERE userID = %s"
            values = (userID, )
            cursor.execute(sql, values)
            result = cursor.fetchall()

            if not result:
                return None

            returnvalue = self.convertToDictionaryPatterns(result)
            return returnvalue
        
        except Exception as e:
            print(f"Database error in findByUserID: {e}")
            raise
        finally:
            self.closeAll()
    
# Create a pattern
    def create(self, pattern):
        try:
            cursor = self.getCursor()
            sql = "INSERT INTO patterns (patternID, brand, category, fabric_type, description, format, userID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = [pattern['patternID'], pattern['brand'], pattern['category'], pattern['fabric_type'], pattern['description'], pattern['format'], pattern['userID']]
            cursor.execute(sql, values)
            self.connection.commit()
            newid = cursor.lastrowid
            return newid
        except Exception as e:
            print(f"Database error in create: {e}")
            raise
        finally:
            self.closeAll()
    
# Update a pattern
    def update(self, pattern):
        try:
            cursor = self.getCursor()
            sql = "UPDATE patterns SET brand = %s, category = %s, fabric_type = %s, description = %s, format = %s, userID= %s WHERE patternID = %s"
            values = (pattern.get("brand"), pattern.get("category"), pattern.get("fabric_type"), pattern.get("description"), pattern.get('format'), pattern.get('userID'), pattern.get("patternID"))
            cursor.execute(sql, values)
            self.connection.commit()
            return pattern
        except Exception as e:
            print(f"Database error in update: {e}")
            raise
        finally:
            self.closeAll()

# Delete
    def delete(self, patternID):
        try:
            cursor = self.getCursor()
            sql = "DELETE FROM patterns WHERE patternID = %s"
            values = (patternID, )
            cursor.execute(sql, values)
            self.connection.commit()
            print("Pattern deleted")
        except Exception as e:
            print(f"Database error in delete: {e}")
            raise
        finally:
            self.closeAll()


    def get_all_users(self):
        try:
            cursor = self.getCursor()
            sql = "SELECT userID, first_name, last_name, email FROM users"
            cursor.execute(sql)
            results = cursor.fetchall()

            if not results:
                return None
            
            users = []
            for row in results:
                users.append(self.convertToDictionaryUsers(row))
            self.closeAll()
            return users
        except Exception as e:
            print(f"Database error in get_all_users: {e}")
            raise
        finally:
            self.closeAll()

    
    def create_user(self, user):
        try:
            cursor = self.getCursor()
            sql = "INSERT INTO users (first_name, last_name, email, password_hash) VALUES (%s, %s, %s, %s)"
            values = (user.get("first_name"), user.get("last_name"), user.get("email"), user.get("password"))
            cursor.execute(sql, values)
            self.connection.commit()
            newid = cursor.lastrowid
            user['userID'] = newid
            return user
        
        except Exception as e:
            print(f"Database error in create_user: {e}")
            raise
        finally:
            self.closeAll()
    
    def update_user(self, user):
        try:
            cursor = self.getCursor()
            sql = "UPDATE users SET first_name = %s, last_name = %s, email = %s, password_hash = %s WHERE userID = %s"
            values = (user.get("first_name"), user.get("last_name"), user.get("email"), user.get("password"), user.get("userID"))
            cursor.execute(sql, values)
            self.connection.commit()
            return user
        
        except Exception as e:
            print(f"Database error in update_user: {e}")
            raise
        finally:
            self.closeAll()

    def findByUserID_users(self, userID):
        try:
            cursor = self.getCursor()
            sql = "SELECT userID, first_name, last_name, email FROM users WHERE userID = %s"
            values = (userID, )
            cursor.execute(sql, values)
            result = cursor.fetchall()
            returnvalue = self.convertToDictionaryUsers(result)
            return returnvalue
        except Exception as e:
            print(f"Database error in findByUserID_users: {e}")
            raise
        finally:
            self.closeAll()

    def delete_user(self, userID):
        try:
            cursor = self.getCursor()
            sql = "DELETE FROM users WHERE userID = %s"
            values = (userID, )
            cursor.execute(sql, values)
            self.connection.commit()
            print("User deleted")
        except Exception as e:
            print(f"Database error in delete_user: {e}")
            raise
        finally:
            self.closeAll()

    # Check user exists
    #def user_exists(self, userID):
    #    for user in self.users:
    #        if user["userID"] == userID:
    #            return True
    #    return False

# Borrow a pattern
    def create_borrow_request(self, borrow):
        try:
            cursor = self.getCursor()
            sql = "INSERT INTO borrow_request (loadID, userID, patternID) VALUES (%s, %s, %s) "
            values = [borrow['loadID'], borrow['userID'], borrow['patternID']]
            cursor.execute(sql, values)
            self.connection.commit()
            newid = cursor.lastrowid
            return newid
        except Exception as e:
            print(f"Database error in create_borrow_request: {e}")
            raise
        finally:
            self.closeAll()


patternDAO = PatternDAO()