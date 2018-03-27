from flask import jsonify

class MessagesDAO:
    def __init__(self):
        self.data = []
        self.data.append(Message(3432, "Hey", 20, 123).toDict())
        self.data.append(Message(3433, "Dimelo", 13, 123).toDict())
        self.data.append(Message(3434, "Comemos en Denny's hoy?", 20, 123).toDict())
        self.data.append(Message(3435, "Dale sii", 13, 123).toDict())
        self.size = len(self.data)
        
    
    def getAllMessages(self, gName):
        if(gName == "Wombo-Combo"):
            return self.data
        else:
            return None
        
    def getMessage(self, gName, id):
        if(gName == "Wombo-Combo"):
            for m in self.data:
                if id == m['id']:
                    return m
            return None
        else:
            return None
    
    def postMessage(self, gName, content, uID):
        if(gName == "Wombo-Combo"):
            m = Message(self.data[self.size - 1]['id'] + 1, content, uID, 123).toDict()
            self.data.append(m)
            return m
        else:
            return None


class Message:
    def __init__(self, mID, cont, wID, gID):
        
        self.messageID = mID
        self.content = cont
        self.writerID = wID
        self.groupID = gID
        self.reaction = ""
    
    def getText(self):
        return self.content
    
    def getWriter(self):
        return self.writerID
    
    def getGroup(self):
        return self.groupID
    
    def getID(self):
        return self.messageID
    
    def getReaction(self):
        return self.reaction
    
    def setReaction(self, r):
        self.reaction = r
    
    def toDict(self):
        M = {}
        M['id'] = self.getID()
        M['writerID'] = self.getWriter()
        M['groupID'] = self.getGroup()
        M['content'] = self.getText()
        M['reaction'] = self.getReaction()
        return M
