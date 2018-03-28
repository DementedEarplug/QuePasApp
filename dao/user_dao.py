class UserDAO:
    def __init__(self):
        # I believe users will only have one phone and or one email -MFR
        user1= User(7001, 'Gabriel', 'Reyes', 'Reaper', 'Talon1288', '666-006-0606','Reaper@talon.com')
        user2= User(4405, 'Brigitte', 'Lindholm', 'Squire97', 'EgineeringForevel12', '756-225-8465','brigittaDaPitta12@gmail.com')
        user3= User(8569, 'Shao', 'Kahn', 'KingOfKings', 'NeatherRealm178', '945-785-6428','getTheHuemans33@yahoo.com')
        user4= User(5567, 'Sonya', 'Blade', 'Kissshot', 'Jaxx9887', '452-017-2972','bolndie1288@gmail.com')
        

        self.data = []
        self.data.append(user1.mapUserToDict())
        self.data.append(user2.mapUserToDict())
        self.data.append(user3.mapUserToDict())
        self.data.append(user4.mapUserToDict())

    def getAllUsers(self):
        return self.data

    def getAllUsernames(self):
        usernames = []
        for r in self.data:
            usernames.append(r['username'])
        return usernames
    
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

#User class detailing all the attributes it contains    
class User:
    def __init__(self,IdUser, uFirstName,uLastname, username, password,phone, email):
        self.IdUser = IdUser
        self.uFirstName = uFirstName
        self.uLastname = uLastname
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
    
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
        return mappedUser
