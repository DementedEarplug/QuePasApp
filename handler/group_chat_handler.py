from flask_restful import Resource
from flask import jsonify, request
from flask_restful import reqparse
from dao.group_chat_dao import ChatDAO
from dao.group_participants_dao import ParticipantsDao
from dao.user_dao import UserDAO


#instance of Chat DAO

def mapToDict(row):
    mappedGroup = {}
    mappedGroup['groupId'] = row[0]
    mappedGroup['groupName'] = row[1]
    mappedGroup['ownerId'] = row[2]
    return mappedGroup

def mapOwnertoDict(row):
    mappedUser = {}
    mappedUser['userId'] = row[0]
    mappedUser['FirstName'] = row[1]
    mappedUser['Lastname'] = row[2]
    mappedUser['username'] = row[3]
    # mappedUser['userPassword'] = row[4]
    mappedUser['phoneNumber'] = row[4]
    mappedUser['email'] = row[5]
    return mappedUser

#The way i believe this works is that each route has their own get post put etc... operations
#So we create a handler for each route
#if there are multiple gets for instance, define a different method for each one and
#inside the get method decide which one will be used

def isInList(uid): ##checks if user exists in udao
    udao = UserDAO()
    user = udao.getUserById(uid)
    return user

## for /QuePasApp/groups route
# Finds all groups in the system.
class GroupHandler(Resource):
    def get(self):
        dao = ChatDAO()
        groupList = dao.getGroups()
        resultList = []
        for row in groupList:
            result = mapToDict(row)
            resultList.append(result)
        if(len(resultList)!=0):
            return {"Groups":groupList},200
        else:
            return {"Error":"No Groups Created yet"},404
    
class JoinGroupHandler(Resource):
    def post(self, groupId, userId):
        dao = ChatDAO()
        resp = dao.addUserToGroup(userId, groupId)
        if resp==201:
            return {"Message":"User added to group","User Id":userId, "Group Id":groupId}, resp
        elif(resp == 403):
            return {"Error":"User Already Member of group"}, resp
        else:
            return {"Error": "User or Group Not Found"}, resp

#for /QuePasApp/groups/<int:id>
class GroupByIndexHandler(Resource):
    def get(self, groupId): #get group by id
        dao = ChatDAO()
        row = dao.getGroupByID(groupId)
        if not row:
            return {"Error":"Group not found"},404
        else:
            group= mapToDict(row)
            return jsonify(Group= group)

    def delete(self, id): #delete group by id
        dao = ChatDAO()
        result = dao.deleteGroupByID(id)
        return result

#for /QuePasApp/groups/user/<int:userID>        
class GroupByOwnerHandler(Resource):
    def get(self, userId): #get groups by user id
        dao = ChatDAO()

        inList = isInList(userId)
        ##if not in list end
        if not(inList):
            #print('Here')
            return {"Error":"User not found"}, 404
        
        ##get groups by owner
        result = dao.getGroupsByAdminID(userId)
        
        ##if user does not owns a group
        if(len(result) == 0):
            return {"Error":"User is not member of any group"}
        
        return jsonify(Groups = result) ##returns all groups where user is the owner
#for /QuePasApp/groups/new
class CreateGroupHandler(Resource):
    def post(self):
        dao = ChatDAO()
        return dao.createGroup(request.form['groupName'], request.form['ownerId'])

# for /QuePasApp/groups/<int:groupId>/removeUser/<int:userId>
class RemoveUser(Resource):
    def post(self, groupId, userId):
        dao = ChatDAO()
        return dao.removeUser(groupId, userId)

#for /QuePasApp/groups/user/<int:userID>        
class GroupParticipantsHandler(Resource):
    
    def get(self, groupID):
        dao = ChatDAO()
        pdao = ParticipantsDao()
        group = dao.getGroupByID(groupID)
        if (len(group) == 0):
            return {"Error":"group does not exists"}, 404
        
        result = pdao.getParticipantsOfGroupById(groupID)
        if(len(result) ==  0):
            return {"Error":"Group Does not have any participant (weird)"}, 404
        return jsonify(Participants = result)
#for /QuePasApp/users/<int:userID>/groups/
class UserGroupsHandler(Resource): #Get all groups where user is participant
    def get(self, userId):
        dao = ChatDAO()
        result = dao.getGroupsByUserID(userId)
        if(len(result) == 0):
            return {"Error":"User does not belongs to any group"}, 404
        groupList = []
        for row in result:
            groupList.append(mapToDict(row))
        return jsonify(Groups = groupList)

#for /QuePasApp/groups/<int:groupId>/owner/
class GroupOwnerHandler(Resource): #Get owner of group
    def get(self, groupId):
        dao = ChatDAO()

        groups = dao.getGroupOwner(groupId)
        if not groups: #dao.getgroupbyis to test if the group exists.
            return {"Error":"Group Not Found"},404
        else:
            resultList=[]
            for row in groups:
                result = mapOwnertoDict(row)
                resultList.append(result)
            return jsonify(GroupOwner=resultList)

