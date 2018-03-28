from flask import jsonify, request
from dao.user_dao import UserDAO 
from flask_restful import Resource, reqparse


#Construct DAO instance
dao = UserDAO()

def mapToDict(row):
        result = {}
        result['IdUser'] = row[0]
        result['uFirstName'] = row[1]
        result['uLastname'] = row[2]
        result['username'] = row[3]
        result['password'] = row[4]
        result['phone'] = row[5]
        result['email'] = row[6]
       #result['contactList'] = row[7]
        return result

class UserHandler(Resource):
	def get(self):
		result = dao.getAllUsers()
		return jsonify(User = result)

class UserByIdHandler(Resource):
	def get(self, IdUser):
		result = dao.getUserById(IdUser)
		if result == None:
			return jsonify("NOT FOUND"), 404
		else:
			return jsonify(User = result)

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
        user = dao.searchByUsername(username)
        return jsonify(User = user)

class UsernameHandler(Resource):
    def get(self):
        result= dao.getAllUsernames()
        return result
#UserContactsHandler