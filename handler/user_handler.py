from flask import jsonify, request
from dao.user_dao import UserDAO 
from dao.contactlist_dao import ContactlistDAO
from flask_restful import Resource, reqparse


#Construct DAO instance
dao = UserDAO()
cDao = ContactlistDAO()

def map_to_dict(self, row):
    result = {}
    mappedUser['userId'] = self.getID()
    mappedUser['uFirstName'] = self.getFirstName()
    mappedUser['uLastname'] = self.getLastName()
    mappedUser['username'] = self.getUsername()
    mappedUser['password'] = self.getPassword()
    mappedUser['phone'] = self.getPhone()
    mappedUser['email'] = self.getEmail()
    mappedUser['contacts'] = self.getContacts()

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
        return jsonify( Usernames = result)
#UserContactsHandler

class ContactListHandler(Resource):
     def get(self,IdUser):
         result = cDao.getAllContacts(IdUser)
         return jsonify(Contacts = result)