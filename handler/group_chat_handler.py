from flask_restful import Resource
from flask import jsonify
from flask_restful import reqparse
from dao.group_chat_dao import ChatDAO


#instance of Chat DAO
dao = ChatDAO()

#The way i believe this works is that each route has their own get post put etc... operations
#So we create a handler for each route
#if there are multiple gets for instance, define a different method for each one and
#inside the get method decide which one will be used

## for /api/groups route
class GroupHandler(Resource):

    def get(self): #get all groups
        result = dao.getGroups()
        return result
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

#for /api/groups/<int:id>
class GroupByIndexHandler(Resource):
    def get(self, id): #get group by id
        result = dao.getGroupByID(id)
        return result
    def delete(self, id): #delet group by id
        result = dao.deleteGroupByID(id)
        return result

#for /api/groups/user/<int:userID>        
class GroupByUserHandler(Resource):
    def get(self, userID): #get groups by user id
        result = dao.getGroupsByUserID(userID)
        return result
    
