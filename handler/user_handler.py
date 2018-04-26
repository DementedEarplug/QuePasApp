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
    #Returns all the users in the system
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
    # Returns info of a user with a given ID
    def get(self, userId):
        row = dao.getUserById(userId)
        if not row:
            return jsonify(Error="User with id: %s not gound"%userId),404
        else:
            user= mapToDict(row)
            return jsonify(User= user)

class UserByNameHandler(Resource):
    def get(self, uFirstName):
        row = dao.searchByName(uFirstName)
        if not row:
            return jsonify(Error="User with First Name: %s not gound"%uFirstName),404
        else:
            user= mapToDict(row)
            return jsonify(User= user)

    

class UserByLastNameHandler(Resource):
    def get(self, uLastname):
        row = dao.searchByLName(uLastname)
        if not row:
            return jsonify(Error="User with Last Name: %s not gound"%uLastname),404
        else:
            user= mapToDict(row)
            return jsonify(User= user)

class GetByUsernameHandler(Resource):
    def get(self, username):
        row = dao.searchByUsername(username)
        if not row:
            return jsonify(Error="User with username: %s not gound"%username),404
        else:
            user= mapToDict(row)
            return jsonify(User= user)


class ContactListHandler(Resource):
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