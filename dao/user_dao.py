import psycopg2
from config import db_config
 
class UserDAO:
    def __init__(self):
        #maybe jsut add el url del DB directly?
        connection_url = "dbname=%s user=%s password=%s" % (db_config['dbname'],  db_config['user'], db_config['passwd'])
        self.conn = psycopg2._connect('postgres://rdoycbxokxgmsz:d9980f20415499517e3caacaa67ee00376d331677988af4b8c4887fc65235efc@ec2-75-101-142-91.compute-1.amazonaws.com:5432/d2o9j3bddfg00r')
        
    # Displays all the users in the system with their information.
    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = 'select userId, FirstName, LastName, username, phoneNumber, email from users;'
        cursor.execute(query)
        result = []
        for ror in cursor:
            result.append(ror)
        return result
    
    def addUser(self, uName, uLName, username, passwd, phoneNumber, email):
        cursor = self.conn.cursor()
        q1 = "Select Case when (select count(*) from users where email = %s )>0 "
        q2 =  "then \'yes\' else \'no\' end as emailTest, "
        q3 = "Case when (select count(*) from users where username = %s )>0 "
        q4 = "then \'yes\' else \'no\' end as usernameTest, "
        q5 = "Case when (select count(*) from users where phonenumber = %s )>0 "
        q6 = "then \'yes\' else \'no\' end as phoneTest from users group by emailTest"
        query = q1 + q2 + q3 + q4 + q5 + q6
        cursor.execute(query, [email, username, phoneNumber])
        conflicts = cursor.fetchone()
        if (conflicts[0]=='yes'):
            return 'email already registered',403
        elif(conflicts[1]=='yes'):
            return 'username already taken',403
        elif(conflicts[2]=='yes'):
            return 'phonenumber is already registered', 403
        else:
            query = 'insert into users (firstname, lastname, username, userpassword, phonenumber, email) values(%s, %s, %s, %s, %s, %s)'
            cursor.execute(query, [uName, uLName, username, passwd, phoneNumber, email])
            self.conn.commit()
            return 'user created',201
        # else:
        #     return 403

    # Displays all the users in the system with their information.
    def getAllUsersByChat(self, groupId):
        cursor = self.conn.cursor()
        query = 'select userId, FirstName, LastName, username, phoneNumber, email from users natural inner join participants where groupId = %s;'
        cursor.execute(query,(groupId,))
        result = []
        for ror in cursor:
            result.append(ror)
        return result

    # Search user info given a user id.
    def getUserById(self, userId):
        cursor = self.conn.cursor()
        query = "select userId, FirstName, LastName, username, phoneNumber, email from users where userId = %s ;"
        cursor.execute(query,(userId,))
        result = cursor.fetchone()
        return result

    # Search user info given the name of a user.
    def searchByName(self, name):
        cursor = self.conn.cursor()
        query = "select userId, FirstName, LastName, username, phoneNumber, email from users where FirstName = %s ;"
        cursor.execute(query,(name,))
        result = cursor.fetchone()
        return result

    # Search user info given username.
    def searchByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select userId, FirstName, LastName, username, phoneNumber, email from users where username = %s ;"
        cursor.execute(query,(username,))
        result = cursor.fetchone()
        return result

    # Search user info given the lastname of a user.
    def searchByLName(self, Lname):
        cursor = self.conn.cursor()
        query = "select userId, FirstName, LastName, username, phoneNumber, email from users where LastName = %s ;"
        cursor.execute(query,(Lname,))
        result = cursor.fetchone()
        return result
    
    # Search user by email and password
    def login(self, email, password):
        cursor = self.conn.cursor()
        query = "select userId, FirstName, LastName, username, phoneNumber, email from users where email = %s and userPassword = %s;"
        cursor.execute(query,(email, password,))
        result = cursor.fetchone()
        return result
