from flask import jsonify, request
from dao.user_dao import UserDAO 
from dao.contactlist_dao import ContactlistDAO
from flask_restful import Resource, reqparse


#Construct DAO instance
dao = UserDAO()
cDao = ContactlistDAO()

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

class UserHandler(Resource):
    def get(self):
        userList = dao.getAllUsers()
        resultList = []
        for row in userList:
            result = mapToDict(row)
            resultList.append(result)
        if (len(resultList)!=0):
            return jsonify(User= resultList)
        else:
            return jsonify("NOT FOUND"), 404

class UserByIdHandler(Resource):
    def get(self, userId):
        row = dao.getUserById(userId)
        if not row:
            return jsonify(Error="User with id: %s not gound"%userId),404
        else:
            user= mapToDict(row)
            return jsonify(User= user)

class UserByNameHandler(Resource):
    def get(self, uFirstName):
        user = dao.searchByName(uFirstName)
        return jsonify(User = user)

    

class UserByLastNameHandler(Resource):
    def get(self, uLastname):
        user = dao.searchByLName(uLastname)
        return jsonify(User = user)

class GetByUsernameHandler(Resource):
    def get(self, username):
        row = dao.searchByUsername(username)
        if not row:
            return jsonify(Error="User with username: %s not gound"%username),404
        else:
            user= mapToDict(row)
            return jsonify(User= user)

class UsernameHandler(Resource):
    def get(self):
        result= dao.getAllUsernames()
        return jsonify( Usernames = result)
#UserContactsHandler

class ContactListHandler(Resource):
     def get(self,userId):
         result = cDao.getAllContacts(userId)
         return jsonify(Contacts = result)