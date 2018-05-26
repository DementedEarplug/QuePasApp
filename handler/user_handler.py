from flask import jsonify, request
from dao.user_dao import UserDAO 
from dao.contactlist_dao import ContactlistDAO
from flask_restful import Resource, reqparse


#Construct DAO instances

cDao = ContactlistDAO() #needed to find the contacts.

#Function to map the result of a query into a dictionary.
def mapToDict(row):
    mappedUser = {}
    mappedUser['userId'] = row[0]
    mappedUser['FirstName'] = row[1]
    mappedUser['Lastname'] = row[2]
    mappedUser['username'] = row[3]
    # mappedUser['userPassword'] = row[4]
    mappedUser['phoneNumber'] = row[4]
    mappedUser['email'] = row[5]
    return mappedUser

def mapActiveUsers(row):
    result = []
    mappedUser = {}
    mappedUser['postdate'] = row[0]
    mappedUser['count'] = row[1]
    return mappedUser
class UserHandler(Resource):
    #Returns all the users in the system
    def get(self):
        dao = UserDAO()
        userList = dao.getAllUsers()
        resultList = []
        for row in userList:
            result = mapToDict(row)
            resultList.append(result)
        if (len(resultList)!=0):
            return jsonify(Users= resultList)
        else:
            return jsonify("NOT FOUND"), 404
class AddUserHandler(Resource):
    def post(self):
        dao = UserDAO()
        resp = dao.addUser(request.form['name'], request.form['lastname'], request.form['username'], request.form['password'], request.form['phonenumber'], request.form['email'])
        return resp 

class ActiveUsersHandler(Resource):
    def get(self):
        dao = UserDAO()
        activeUsers = dao.getActiveUsers()
        result = []
        for row in activeUsers:
            temp = mapActiveUsers(row)
            result.append(temp)
        if (len(result)!=0):
            return jsonify(ActiveUsers= result)
        else:
            return jsonify("NOT FOUND"), 404
        

class UsersInGroupHandler(Resource):
    #Returns all the users in the system
    def get(self, groupId):
        dao = UserDAO()
        userList = dao.getAllUsersByChat(groupId)
        resultList = []
        for row in userList:
            result = mapToDict(row)
            resultList.append(result)
        if (len(resultList)!=0):
            return jsonify(Users= resultList)
        else:
            return jsonify("NOT FOUND"), 404

class UserByIdHandler(Resource):
    # Returns info of a user with a given ID
    def get(self, userId):
        dao = UserDAO()
        row = dao.getUserById(userId)
        if not row:
            return jsonify(Error="User with id: %s not gound"%userId),404
        else:
            user= mapToDict(row)
            return jsonify(User= user)

class UserByNameHandler(Resource):
    # Search a user with a given firstname.
    def get(self, uFirstName):
        dao = UserDAO()
        row = dao.searchByName(uFirstName)
        if not row:
            return jsonify(Error="User with First Name: %s not found"%uFirstName),404
        else:
            user= mapToDict(row)
            return jsonify(User= user)

    

class UserByLastNameHandler(Resource):
    # Search a user with a given lastname.
    def get(self, uLastname):
        dao = UserDAO()
        row = dao.searchByLName(uLastname)
        if not row:
            return jsonify(Error="User with Last Name: %s not found"%uLastname),404
        else:
            user= mapToDict(row)
            return jsonify(User= user)

class GetByUsernameHandler(Resource):
    # Search a user with a given username.
    def get(self, username):
        dao = UserDAO()
        row = dao.searchByUsername(username)
        if not row:
            return jsonify(Error="User with username: %s not found"%username),404
        else:
            user= mapToDict(row)
            return jsonify(User= user)


class ContactListHandler(Resource):
    #Gets the contact list of the user with userId = ownerId.
     def get(self,ownerId):
        userList = cDao.getAllContacts(ownerId)
        resultList = []
        for row in userList:
            result = mapToDict(row)
            resultList.append(result)
        if (len(resultList)!=0):
            return jsonify(Contacts= resultList)
        else:
            return jsonify("NOT FOUND"), 404
        
class UserLoginHandler(Resource):
    # Search a user with a given username.
    def post(self):
        dao = UserDAO()
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, location = 'json')
        parser.add_argument('password', type=str, location = 'json')
        args = parser.parse_args(strict=True)
        
        row = dao.login(args['email'], args['password'])
        if not row:
            return {'Error' : "Invalid Login"},404
        else:
            user= mapToDict(row)
            return jsonify(User= user)