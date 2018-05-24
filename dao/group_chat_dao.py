from flask import jsonify
from dao.user_dao import UserDAO
from config import db_config
import psycopg2

class ChatDAO:
    def __init__(self):
        #maybe jsut add el url del DB directly?
        connection_url = "dbname=%s user=%s password=%s" % (db_config['dbname'],  db_config['user'], db_config['passwd'])
        self.conn = psycopg2._connect('postgres://rdoycbxokxgmsz:d9980f20415499517e3caacaa67ee00376d331677988af4b8c4887fc65235efc@ec2-75-101-142-91.compute-1.amazonaws.com:5432/d2o9j3bddfg00r')
    
    def getGroupByID(self, groupId):
        cursor = self.conn.cursor()
        query = "select groupName, groupId, ownerId from groups where groupId = %s ;"
        cursor.execute(query,(groupId,))
        result = cursor.fetchone()
        return result

    def getGroupsByUserID(self, userId):
        cursor = self.conn.cursor()
        query = "select groupId, groupName, ownerId from groups natural inner join participants natural inner join users where userId = %s;"
        cursor.execute(query,(userId,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        #  result = {}
        # for g in self.data:
        #     if g['userID']==userID:
        #         result[g['id']]=g
        # return result


    def getUserGroups(self, userID):
        result = []
        groups = self.getGroups() #Get all groups
        for group in groups:
            gpar = participants[groups[group]['id']] #get participants of group
            if userID in gpar: #When user is participant of group
                result.append(group)
        return result


    def addGroup(self, id, name, userID):
        group1={'id':id,'name':name,'userID':userID}
        for g in self.data:
            if g['id']==id:
                return {}
        self.data.append(group1)
        print(self.data)
        return group1

    # Get all groups in the system
    def getGroups(self):
        cursor = self.conn.cursor()
        query = 'select * from groups;'
        cursor.execute(query)
        result = []
        for ror in cursor:
            result.append(ror)
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
        
    def getGroupOwner(self, groupId):
        cursor = self.conn.cursor()
        query = 'select userId, FirstName,Lastname, username, phonenumber, email from groups inner join users on ownerId = userId where groupId = %s ;'
        cursor.execute(query,(groupId,))
        result = []
        for ror in cursor:
            result.append(ror)
        return result


