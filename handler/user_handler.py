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
            return {"Error": " Not Found"}, 404
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
            return {"Error": " Not Found"}, 404
        

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
            return {"Error": "Not Found"}, 404

class UserByIdHandler(Resource):
    # Returns info of a user with a given ID
    def get(self, userId):
        dao = UserDAO()
        row = dao.getUserById(userId)
        # print(row)
        if(row):
            user= mapToDict(row)
            return jsonify(User= user)
        else:
            return {"Error": "User Not Found"}, 404
            

class UserByNameHandler(Resource):
    # Search a user with a given firstname.
    def get(self, uFirstName):
        dao = UserDAO()
        row = dao.searchByName(uFirstName)
        if not row:
            return {"Error": "User Not Found"}, 404
        else:
            userList = []
            for u in row:
                user= mapToDict(u)
                userList.append(user)
            return jsonify(User= userList)

    

class UserByLastNameHandler(Resource):
    # Search a user with a given lastname.
    def get(self, uLastname):
        dao = UserDAO()
        row = dao.searchByLName(uLastname)
        if not row:
            return {"Error": "User Not Found"}, 404
        else:
            userList = []
            for u in row:
                user= mapToDict(u)
                userList.append(user)
            return jsonify(User= userList)

class GetByUsernameHandler(Resource):
    # Search a user with a given username.
    def get(self, username):
        dao = UserDAO()
        row = dao.searchByUsername(username)
        if not row:
            return {"Error": " User Not Found"}, 404
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
            return {"Error": " Not Found"}, 404
    def post(self, ownerId):
        
        info = {"phone":request.form['phone'] or 'None', "email":request.form['email'] or 'None'}
        print(info['phone'])
        result = cDao.addToContact(ownerId, info), 201
        if(result.__contains__("Can't")):
            return {"Error":result}, 404
        else:
            return {"Message":result}, 201
        
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