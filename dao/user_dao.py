import psycopg2
from config import db_config
 
class UserDAO:
    def __init__(self):
        #maybe jsut add el url del DB directly?
        connection_url = "dbname=%s user=%s password=%s" % (db_config['dbname'],  db_config['user'], db_config['passwd'])
        self.conn = psycopg2._connect('postgres://ekabibbfjhmljk:ea67f5fef908e608149d9ebbdffa8fc365f8178649299422e5fa91c5c9e1eaf6@ec2-54-163-240-54.compute-1.amazonaws.com:5432/dfsgi0mppudcls')
        

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = 'select userId, FirstName, LastName, username, phoneNumber, email from users;'
        cursor.execute(query)
        result = []
        for ror in cursor:
            result.append(ror)
        return result

    def getUserById(self, userId):
        cursor = self.conn.cursor()
        query = "select userId, FirstName, LastName, username, phoneNumber, email from users where userId = %s ;"
        cursor.execute(query,(userId,))
        result = cursor.fetchone()
        return result

    #need to add one to get contacts

    def searchByName(self, name):
        cursor = self.conn.cursor()
        query = "select userId, FirstName, LastName, username, phoneNumber, email from users where FirstName = %s ;"
        cursor.execute(query,(name,))
        result = cursor.fetchone()
        return result

    def searchByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select userId, FirstName, LastName, username, phoneNumber, email from users where username = %s ;"
        cursor.execute(query,(username,))
        result = cursor.fetchone()
        return result

    def searchByLName(self, Lname):
        cursor = self.conn.cursor()
        query = "select userId, FirstName, LastName, username, phoneNumber, email from users where LastName = %s ;"
        cursor.execute(query,(Lname,))
        result = cursor.fetchone()
        return result
