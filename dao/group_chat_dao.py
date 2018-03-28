from flask import jsonify
from dao.user_dao import UserDAO
class ChatDAO:
    def __init__(self):
        self.udao = UserDAO()
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
        result = {}
        for g in self.data:
            if g['userID']==userID:
                result[g['id']]=g
        return jsonify(result)

    def addGroup(self, id, name, userID):
        group1={'id':id,'name':name,'userID':userID}
        for g in self.data:
            if g['id']==id:
                return {}
        self.data.append(group1)
        print(self.data)
        return group1

    def getGroups(self):
        result = {}
        for g in self.data:
           result[g['id']]=g
        return result

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
    def getGroupOwner(self, id):
        uid = self.getGroupByID(id)['userID']
        user = self.udao.getUserById(uid)
        return user

