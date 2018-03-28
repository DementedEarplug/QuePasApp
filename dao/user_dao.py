class UserDAO:
    def __init__(self):
        # I believe users will only have one phone and or one email -MFR
        user1=[7001, 'Gabriel', 'Reyes', 'Reaper', 'Talon1288', '666-006-0606','Reaper@talon.com', 1234] 
        user2=[4405, 'Brigitte', 'Lindholm', 'Squire97', 'EgineeringForevel12', '756-225-8465','brigittaDaPitta12@gmail.com',4567]
        user3=[8569, 'Shao', 'Kahn', 'KingOfKings', 'NeatherRealm178', '945-785-6428','getTheHuemans33@yahoo.com',7890]
        user4=[5567, 'Sonya', 'Blade', 'Kissshot', 'Jaxx9887', '452-017-2972','bolndie1288@gmail.com',9012]
        

        self.data = []
        self.data.append(user1)
        self.data.append(user2)
        self.data.append(user3)
        self.data.append(user4)
    
    def getAllUsers(self):
        return self.data
    
    def getUserById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    #need to add one to get contacts

    def searchByName(self, name):
        result = []
        for r in self.data:
            if name.lower() == r[1].lower():
                result.append(r)
        return result

    def searchByLastName(self, lName):
            result = []
            for r in self.data:
                if lName.lower() == r[2].lower():
                    result.append(r)
            return result
    
            