from flask import jsonify
import time

#Message Data Access object that retrieves data from the DB (currently hardcoded)
class MessagesDAO:
    #Hardcoded message data corresponding to one group chat is created
    def __init__(self):
        self.data = []
        
        groupA = []
        #Wombo-Combo['groupID'] = 123
        groupA.append(Message(3432, "Hey", 20, 123, "03/27/2018", "00:03:05").toDict())
        groupA.append(Message(3433, "Dimelo", 13, 123, "03/27/2018", "00:03:30").toDict())
        groupA.append(Message(3434, "Comemos en Denny's hoy?", 20, 123, "03/27/2018", "00:04:00").toDict())
        groupA.append(Message(3435, "Dale sii", 13, 123, "03/27/2018", "00:05:00").toDict())
        self.data.append(groupA)
        
        groupB = []
        #BestiasICOM['groupID'] = 124
        groupB.append(Message(200, "Acabaste el proyecto?", 23, 124, "03/28/2018", "23:55:05").toDict())
        groupB.append(Message(201, "No, y tu?", 31, 124, "03/28/2018", "23:56:02").toDict())
        groupB.append(Message(202, "No", 23, 124, "03/28/2018", "23:57:10").toDict())
        groupB.append(Message(203, "Nos jodimos", 31, 123, "03/28/2018", "23:58:12").toDict())
        self.data.append(groupB)
        #self.size = len(self.data)
        
        self.groupNames = [
            "Wombo-Combo",
            "BestiasICOM"
            ]
        
        self.groupIds = {
            "Wombo-Combo" : 0,
            "BestiasICOM" : 1
            }
        
    #All messages from all group chats are retrieved
    def getAllMessages(self):
        return self.data
        
    #All messages corresponding to a group chat are retrieved 
    def getGroupMessages(self, gName):
        for g in self.groupNames:
            if g == gName:
                return self.data[self.groupIds[g]]
        return None
        
    #A message that corresponds to the given ID is searched in the corresponding group chat
    def getMessage(self, gName, id):
        for g in self.groupNames:
            if g == gName:
                for m in self.data[self.groupIds[g]]:
                    if id == m['id']:
                        return m
        return None
    
    #A message is posted into the corresponding group chat using the latest message id,
    #a given content, writerID, groupID, and current time and date
    def postMessage(self, gName, content, uID):
        print("Before For")
        for g in self.groupNames:
            print(g)
            if g == gName:
                print("Group Name: " + g)
                group = self.data[self.groupIds[g]]
                print(group)
                groupSize = len(group)
                print("Group Size: " + str(groupSize))
                lastId = group[groupSize - 1]['id']
                print("Last Id: " + str(lastId))
                m = Message(lastId + 1, content, uID, self.groupIds[g], time.strftime("%X"), time.strftime("%x")).toDict()
                group.append(m)
                return m
        return None

#A Message object is defined for easier data manipulation after parsing
class Message:
    #Message object is created using all available parameters
    def __init__(self, mID, cont, wID, gID, postD, postT):     
        self.messageId = mID
        self.content = cont
        self.writerId = wID
        self.groupId = gID
        self.reactions = []
        self.postDate = postD
        self.postTime = postT
        
    #Getters for all of the objects variables
    def getText(self):
        return self.content
    
    def getWriter(self):
        return self.writerId
    
    def getGroup(self):
        return self.groupId
    
    def getID(self):
        return self.messageId
    
    def getReaction(self):
        return self.reactions
    
    def getPostDate(self):
        return self.postDate
    
    def getPostTime(self):
        return self.postTime    
    
    #Adds reactions to the message
    def addReaction(self, r):
        self.reactions.append(r)
    
    #Creates a dictionary from the message object instance
    def toDict(self):
        M = {}
        M['id'] = self.getID()
        M['writerId'] = self.getWriter()
        M['groupId'] = self.getGroup()
        M['content'] = self.getText()
        M['reactions'] = self.getReaction()
        M['postDate'] = self.getPostDate()
        M['postTime'] = self.getPostTime()
        return M
