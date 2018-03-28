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
		mapped_result = []
		for r in result:
			mapped_result.append(mapToDict(r))
		return jsonify(User = mapped_result)

class UserByIdHandler(Resource):
	def get(self, IdUser):
		result = dao.getUserById(IdUser)
		if result == None:
			return jsonify("NOT FOUND"), 404
		else:
			mapped = mapToDict(result)
			return jsonify(User = mapped)

class UserByNameHandler(Resource):
    def get(self, uFirstName):
        user = dao.searchByName(uFirstName)
        mapped = []
        for r in user:

            mapped.append(mapToDict(r))
        return jsonify(User = mapped)

class UserByLastNameHandler(Resource):
    def get(self, uLastname):
        user = dao.searchByLastName(uLastname)
        mapped = []
        for r in user:

            mapped.append(mapToDict(r))
        return jsonify(User = mapped)

    
