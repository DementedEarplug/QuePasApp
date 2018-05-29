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
        query = '''select
        case when (select count(*) from groups where groupid = %s)>0 then 'yes' else 'no' end,
        case when (select count(*) from users where userid = %s)>0 then 'yes' else 'no' end, count(*)
        from participants where userid = %s and groupid = %s;
        '''
        cursor.execute(query, [gid,uid,uid, gid])
        result = cursor.fetchone()
        if(result[2]==0 and result[0]=='yes' and result[1]=='yes'): #if user is not in group yet

            query = "Insert into participants (userid, groupid) Values(%s, %s)"
            cursor.execute(query, [uid, gid])
            self.conn.commit()
            return 201
        elif(result[2]>0):
            return 403
        elif(result[0]=='no' or result[1]=='no'):
            return 404

    def removeUser(self, groupid, userid):
        cursor = self.conn.cursor()
        #check if user exists and if he is admin of group
        q1 = "select case when "
        q2 = "(select count(*) from groups where ownerid = %s and groupid = %s)>0 " #check if is owner
        q3 = "then 'yes' else 'no' end, "
        q4 = "case when (select count(*) from participants where userid = %s and groupid = %s)>0 " #check if is participant
        q5 = "then 'yes' else 'no' end from users where userid = %s" #check if user exsists
        query = q1+q2+q3+q4+q5
        cursor.execute(query, [userid,groupid, userid, groupid, userid])
        checkUser = cursor.fetchone()
        print(checkUser)
        if(checkUser and checkUser[0]=='no' and checkUser[1]=='yes'):
            query = 'delete from participants where groupid = %s and userid = %s'
            cursor.execute(query,[groupid, userid])
            self.conn.commit()
            return {"Message" :"Participant removed from group"},204
        elif (not checkUser):
            return {"Error":'User does not exists'}, 404
        elif (checkUser[0]=='yes'):
            return {"Error":"can't remove admin from his group"},403
        elif (checkUser[1]=='no'):
            return {"Error":'User is not participant of group'}, 403
        return {'Error':'Well, this is weird'},404

    def createGroup(self, name, ownerId):
        cursor = self.conn.cursor()
        #check if user exists
        query = "select * from users where userid = %s"
        cursor.execute(query, [ownerId])
        checkUser = cursor.fetchone()
        if(checkUser):
            query = "with result as (Insert into groups (groupname, ownerid) values(%s, %s) returning groupid) select groupid from result"
            cursor.execute(query, [name, ownerId])
            groupid = cursor.fetchone()[0]
            self.conn.commit()
            result = {"Message":"Group Created",'groupId':groupid}
            self.addUserToGroup(ownerId, groupid)
            return result, 201
        else:
            return {"Error":"User not found"}, 404


    def getGroupsByUserID(self, userId):
        cursor = self.conn.cursor()
        query = "select groupId, groupName, ownerId from users natural inner join participants natural inner join groups where userid = %s"
        cursor.execute(query,(userId,))
        groups = cursor.fetchall()
        result = []
        for row in groups:
            result.append(row)
        return result
    def getGroupsByAdminID(self, userId):
        cursor = self.conn.cursor()
        query = "select groupId, groupName, ownerId from groups inner join users on userid = ownerId where ownerId = %s;"
        cursor.execute(query,(userId,))
        groups = cursor.fetchall()
        result = []
        for row in groups:
            result.append(row)
        return result

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
        
    def getGroupOwner(self, groupId):
        cursor = self.conn.cursor()
        query = 'select userId, FirstName,Lastname, username, phonenumber, email from groups inner join users on ownerId = userId where groupId = %s ;'
        cursor.execute(query,(groupId,))
        result = []
        for ror in cursor:
            result.append(ror)
        return result


