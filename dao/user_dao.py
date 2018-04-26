import psycopg2
from config import db_config
 
class UserDAO:
    def __init__(self):
        #maybe jsut add el url del DB directly?
        connection_url = "dbname=%s user=%s password=%s" % (db_config['dbname'],  db_config['user'], db_config['passwd'])
        self.conn = psycopg2._connect('postgres://ekabibbfjhmljk:ea67f5fef908e608149d9ebbdffa8fc365f8178649299422e5fa91c5c9e1eaf6@ec2-54-163-240-54.compute-1.amazonaws.com:5432/dfsgi0mppudcls')
        

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = 'select * from users;'
        cursor.execute(query)
        result = []
        for ror in cursor:
            result.append(ror)
        return result

    def getAllUsernames(self):
        username = []
        for r in self.data:
            username.append({'IdUser':r['IdUser'], 'username': r['username']})
        return username
    
    def getUserById(self, id):
        for r in self.data:
            if id == r['IdUser']:
                return r
        return None

    #need to add one to get contacts

    def searchByName(self, name):
        result = []
        for r in self.data:
            if name.lower() == r['uFirstName'].lower():
                result.append(r)
        return result

    def searchByUsername(self, username):
        result = []
        for r in self.data:
            if username == r['username']:
                result.append(r)
        return result

    def searchByLName(self, Lname):
        result = []
        for r in self.data:
            if Lname.lower() == r['uLastname'].lower():
                result.append(r)
        return result

    #def getUserContacts(self,id):
     
     #   result = []
      #  for r in self.data:

#User class detailing all the attributes it contains    
class User():
    def __init__(self,IdUser, uFirstName,uLastname, username, password,phone, email, contacts):
        self.IdUser = IdUser
        self.uFirstName = uFirstName
        self.uLastname = uLastname
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
        self.contacts = contacts
    
    #Define getter functions
    def getID(self):
        return self.IdUser
    
    def getFirstName(self):
        return self.uFirstName
    
    def getLastName(self):
        return self.uLastname
    
    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getPhone(self):
        return self.phone
    
    def getEmail(self):
        return self.email
    
    def getContacts(self):
        return self.contacts

    #Turn attribute into a dictionary
    def mapUserToDict(self):
        mappedUser = {}
        mappedUser['IdUser'] = self.getID()
        mappedUser['uFirstName'] = self.getFirstName()
        mappedUser['uLastname'] = self.getLastName()
        mappedUser['username'] = self.getUsername()
        mappedUser['password'] = self.getPassword()
        mappedUser['phone'] = self.getPhone()
        mappedUser['email'] = self.getEmail()
        mappedUser['contacts'] = self.getContacts()
        return mappedUser
