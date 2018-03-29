from flask_restful import Resource
from flask import jsonify
from flask_restful import reqparse
from dao.group_chat_dao import ChatDAO
from dao.group_participants_dao import ParticipantsDao

from dao.user_dao import UserDAO


#instance of Chat DAO
dao = ChatDAO()

#The way i believe this works is that each route has their own get post put etc... operations
#So we create a handler for each route
#if there are multiple gets for instance, define a different method for each one and
#inside the get method decide which one will be used

def isInList(uid): ##checks if user exists in udao
    udao = UserDAO()
    users = udao.getAllUsers()
    isInList = False
    
    #Check if is in list
    for u in users:
        if uid == u['IdUser']:
            isInList = True
    return isInList

## for /QuePasApp/groups route
class GroupHandler(Resource):

    def get(self): #get all groups
        result = dao.getGroups()
        if len(result)==0:
            return {"Error", "There are no grups yet!"}, 404
        return jsonify(Groups = result)
    def post(self): #add a group using body of request
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location = 'json')
        parser.add_argument('name', type=str, location = 'json')
        parser.add_argument('userID', type=int, location = 'json')
        args = parser.parse_args(strict=True)
        group = {
            'id' : args['id'],
            'name' : args['name'], 
            'userID' : args['userID']
        }
        result = dao.addGroup(group['id'], group['name'], group['userID'])
        return result
    def put(self): #Update the name of a group
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location = 'json')
        parser.add_argument('name', type=str, location = 'json')
        parser.add_argument('userID', type=int, location = 'json')
        args = parser.parse_args(strict=True)
        id = args['id'],
        id = id[0]
        name = args['name'],
        name = name[0] 
        print(id)
        result = dao.changeGroupName(id, name)
        
        return result

#for /QuePasApp/groups/<int:id>
class GroupByIndexHandler(Resource):
    def get(self, id): #get group by id
        result = dao.getGroupByID(id)
        
        if(len(result) == 0): #Group Doesn't exists
            return {"Error": "Group does not exists"}, 404
        
        return jsonify(Group = result) #result contains all the information of the found group

    def delete(self, id): #delete group by id
        result = dao.deleteGroupByID(id)
        return result

#for /QuePasApp/groups/user/<int:userID>        
class GroupByOwnerHandler(Resource):
    def get(self, userID): #get groups by user id
        
        inList = isInList(userID)
        ##if not in list end
        if not(inList):
            print 'Here'
            return {"Error":"User not found"}, 404
        
        ##get groups by owner
        result = dao.getGroupsByUserID(userID)
        
        ##if user does not owns a group
        if(len(result) == 0):
            return {"Error":"User does not owns a group"}
        
        return jsonify(Groups = result) ##returns all groups where user is the owner

#for /QuePasApp/groups/user/<int:userID>        
class GroupParticipantsHandler(Resource):
    
    def get(self, groupID):
        pdao = ParticipantsDao()
        group = dao.getGroupByID(groupID)
        if (len(group) == 0):
            return {"Error":"group does not exists"}, 404
        
        result = pdao.getParticipantsOfGroupById(groupID)
        if(len(result) ==  0):
            return {"Error":"Group Does not have any participant (weird)"}, 404
        return jsonify(Participants = result)
#for /QuePasApp/users/<int:userID>/groups/
class UserGroupsHander(Resource): #Get all groups where user is participant
    def get(self, userID):
        
        inList = isInList(userID)
        ##if not in list end
        if not(inList):
            print 'Here'
            return {"Error":"User not found"}, 404

        result = dao.getUserGroups(userID)
        if(len(result) == 0):
            return {"Error":"User does not belongs to any group"}, 404
        return jsonify(Groups = result)

#for /QuePasApp/groups/<int:groupID>/owner/
class GroupOwnerHandler(Resource): #Get owner of group
    def get(self, groupID):
        group = dao.getGroupByID(groupID)
        if (len(group) == 0):
            return {"Error":"group does not exists"}, 404
        result = dao.getGroupOwner(groupID)
        return jsonify(Owner = result)
