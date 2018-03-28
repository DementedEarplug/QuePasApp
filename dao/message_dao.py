from flask import jsonify
import time

#Message Data Access object that retrieves data from the DB (currently hardcoded)
class MessagesDAO:
    #Hardcoded message data corresponding to one group chat is created
    def __init__(self):
        self.data = []
        self.data.append(Message(3432, "Hey", 20, 123, "00:03:05", "03/27/2018").toDict())
        self.data.append(Message(3433, "Dimelo", 13, 123, "03/27/2018", "00:03:30").toDict())
        self.data.append(Message(3434, "Comemos en Denny's hoy?", 20, 123, "03/27/2018", "00:04:00").toDict())
        self.data.append(Message(3435, "Dale sii", 13, 123, "03/27/2018", "00:05:00").toDict())
        self.size = len(self.data)
        
    #All messages corresponding to the "Wombo-Combo" group chat are retrieved 
    def getAllMessages(self, gName):
        if(gName == "Wombo-Combo"):
            return self.data
        else:
            return None
    #A message that corresponds to the given ID is searched in "Wombo-Combo"
    def getMessage(self, gName, id):
        if(gName == "Wombo-Combo"):
            for m in self.data:
                if id == m['id']:
                    return m
            return None
        else:
            return None
    
    #A message is posted into the "Wombo-Combo" group chat using the latest message id,
    #a given content, writerID, groupID, and current time and date
    def postMessage(self, gName, content, uID):
        if(gName == "Wombo-Combo"):
            m = Message(self.data[self.size - 1]['id'] + 1, content, uID, 123, time.strftime("%X"), time.strftime("%x")).toDict()
            self.data.append(m)
            return m
        else:
            return None

#A Message object is defined for easier data manipulation after parsing
class Message:
    #Message object is created using all available parameters
    def __init__(self, mID, cont, wID, gID, postD, postT):     
        self.messageID = mID
        self.content = cont
        self.writerID = wID
        self.groupID = gID
        self.reactions = []
        self.postDate = postD
        self.postTime = postT
        
    #Getters for all of the objects variables
    def getText(self):
        return self.content
    
    def getWriter(self):
        return self.writerID
    
    def getGroup(self):
        return self.groupID
    
    def getID(self):
        return self.messageID
    
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
        M['writerID'] = self.getWriter()
        M['groupID'] = self.getGroup()
        M['content'] = self.getText()
        M['reactions'] = self.getReaction()
        M['postDate'] = self.getPostDate()
        M['postTime'] = self.getPostTime()
        return M
