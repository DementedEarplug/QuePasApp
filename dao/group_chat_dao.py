from flask import jsonify
class ChatDAO:
    def __init__(self):
        group1={'id':1,'name':'ICOM','userID':7001}
        group2={'id':2,'name':'ICOM','userID':4405}
        self.data = [group1, group2]
    def getGroupByID(self, id):
        result = {}
        for g in self.data:
            if g['id']==id:
               
                result = g
        return result
    def getGroupsByUserID(self, userID):
        result = []
        for g in self.data:
            if g['userID']==userID:
                result.append(g)
        return result

    def addGroup(self, id, name, userID):
        group1={'id':id,'name':name,'userID':userID}
        for g in self.data:
            if g['id']==id:
                return {}
        self.data.append(group1)
        print(self.data)
        return group1

    def getGroups(self):
        print(self.data)
        return self.data

    def changeGroupName(self, id, name):
        group = self.getGroupByID(id)
        group['name'] = name
        return group

    def deleteGroupByID(self, id):
        index = -1
        for i in range(0,len(self.data)):
            
            if(id==self.data[i]['id']):
                index = i        
        return self.data.pop(index)

