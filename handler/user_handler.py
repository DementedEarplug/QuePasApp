from flask import jsonify, request
from dao.user_dao import UserDAO 
from flask_restful import Resource, reqparse


"""class UserHandler:

    def mapToDict(self, row):
        result = {}
        result['IdUser'] = row[0]
        result['uFirstName'] = row[1]
        result['uLastname'] = row[2]
        result['username'] = row[3]
        result['password'] = row[4]
        result['phone'] = row[5]
        result['email'] = row[6]
        return result

    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(User = mapped_result)

    def getUserbyId(self,id):
        dao = UserDAO()
        result = dao.getUserById(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(User = mapped)
    
    def searchUserByName(self, args):
        name = args.get('uFirstName')
        dao = UserDAO()
        result = dao.searchByName(name)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(User=mapped_result)"""

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
        return result

class UserHandler(Resource):
	def get(self):
		result = dao.getAllUsers()
		mapped_result = []
		for r in result:
			mapped_result.append(dao.mapUserToDict(r))
		return jsonify(User = mapped_result)

class UserByIdHandler(Resource):
	def get(self, IdUser):
		result = dao.getUserById(IdUser)
		if result == None:
			return jsonify(Error="NOT FOUND"), 404
		else:
			mapped = dao.mapUserToDict(result)
			return jsonify(User = mapped)

class UserByNameHandler(Resource):
    def get(self, uFirstName):
        user = dao.searchByName(uFirstName)
        mapped = []
        for r in user:
            user = dao.mapUserToDict(r)
            mapped.append(user)
        return jsonify(User = mapped)

    
#UserContactsHandler