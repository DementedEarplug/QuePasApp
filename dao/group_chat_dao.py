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
    def addUserToGroup(self, uid, gid):
        cursor = self.conn.cursor()
        query = "select count(*) from participants where userid = %s and groupid = %s"
        cursor.execute(query, [uid, gid])
        if(cursor.fetchone()[0]==0): #if user is not in group yet

            query = "Insert into participants (userid, groupid) Values(%s, %s)"
            cursor.execute(query, [uid, gid])
            self.conn.commit()
            return 201
        else:
            return 403

    def removeUser(self, groupid, userid):
        cursor = self.conn.cursor()
        #check if user exists and if its admin of group
        q1 = "select case when "
        q2 = "(select count(*) from groups where ownerid = %s and groupid = %s)>0 "
        q3 = "then 'yes' else 'no' end, "
        q4 = "case when (select count(*) from participants where userid = %s and groupid = %s)>0 "
        q5 = "then 'yes' else 'no' end from users where userid = %s"
        query = q1+q2+q3+q4+q5
        cursor.execute(query, [userid,groupid, userid, groupid, userid])
        checkUser = cursor.fetchone()
        print(checkUser)
        if(len(checkUser)>0 and checkUser[0]=='no' and checkUser[1]=='yes'):
            query = 'delete from participants where groupid = %s and userid = %s'
            cursor.execute(query,[groupid, userid])
            self.conn.commit()
            return "Participant removed from group",204
        elif (len(checkUser)==0):
            return 'User does not exists', 404
        elif (checkUser[0]=='yes'):
            return 'can remove admin from his group',403
        elif (checkUser[1]=='no'):
            return 'User is not participant of group', 403
            return 'Well, this is weird'

    def createGroup(self, name, ownerId):
        cursor = self.conn.cursor()
        #check if user exists
        query = "select * from users where userid = %s"
        cursor.execute(query, [ownerId])
        checkUser = cursor.fetchone()
        if(len(checkUser)>0):
            query = "with result as (Insert into groups (groupname, ownerid) values(%s, %s) returning groupid) select groupid from result"
            cursor.execute(query, [name, ownerId])
            groupid = cursor.fetchone()[0]
            self.conn.commit()
            result = {'groupId':groupid}
            return result, 201
        else:
            return 'User not found', 404


    def getGroupsByUserID(self, userId):
        cursor = self.conn.cursor()
        query = "select groupId, groupName, ownerId from groups natural inner join participants natural inner join users where userId = %s;"
        cursor.execute(query,(userId,))
        result = []
        for row in cursor:
            result.append(row)
        return result


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


