from dao.group_chat_dao import ChatDAO
from dao.user_dao import UserDAO
from flask import jsonify
class ParticipantsDao():
    def __init__(self):
        chatDAO = ChatDAO()
        groups = chatDAO.getGroups()
        self.userDAO = UserDAO()
        users = self.userDAO.getAllUsers()
        self.participants = {} 
        self.participants[groups[1]['id']]={
            users[0]['IdUser']: users[0], 
            users[1]['IdUser']: users[1],
            users[2]['IdUser']: users[2]
        }
        self.participants[groups[2]['id']]={
            users[1]['IdUser']: users[1],
            users[3]['IdUser']: users[3],
            users[2]['IdUser']: users[2]
        }
    def getParticipantsOfGroupById(self, id):
        return jsonify(Participants=self.participants[id])
        #if id in self.participants:    
            #return {"Participants": self.participants[id]}
