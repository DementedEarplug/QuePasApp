class UserDAO:
    def __init__(self):
        user1=[7001, 'Gabriel', 'Reyes', 'Reaper', 'Talon1288', ['666-006-0606','225-582-5660'],['g.reyes@ow.gov','Reaper@talon.com']]
        user2=[4405, 'Brigitte', 'Lindholm', 'Squire97', 'EgineeringForevel12', ['756-225-8465'],['brigittaDaPitta12@gmail.com']]
        user3=[8569, 'Shao', 'Kahn', 'KingOfKings', 'NeatherRealm178', ['945-785-6428'],['getTheHuemans33@yahoo.com']]
        user4=[5567, 'Sonya', 'Blade', 'Kissshot', 'Jaxx9887', ['802-016-9510','452-017-2972'],['s.blade@capd.gov','bolndie1288@gmail.com']]

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

    ##def getMessageByUserId(self, id):

    ##def getReactionByUserId(self, id):

    ##def getReplyByUserId(self, id): 
    
    ##def getGroupByUserId(self, id):

    #need to add one to get contacts

    ##def searchByName(self, id)
        