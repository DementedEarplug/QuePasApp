from flask import jsonify, request
from dao.user_dao import UserDAO 

class UserHandler:

    def mapToDict(self, row):
        result = {}
        result['IdUser'] = row[0]
        result['uFirstName'] = row[1]
        result['iLastname'] = row[2]
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
    
    
