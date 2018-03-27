from flask_restful import Resource
from flask import jsonify
from flask_restful import reqparse
from dao.message_dao import MessagesDAO
from test.support import resource

#Construct DAO Instance
#dao = MessageDAO()


#Contains implementation related to all message handling operations of the application

class MessageHandler(Resource):
    def get(self):
        result = dao.getAllMessages(Resource.args().get('gName'))
        if (result != None):
            return jsonify(Messages=result)
        return jsonify(Error="MESSAGES NOT FOUND"), 404
    
class MessageByIdHandler(Resource):
    arguments = Resource.args()
    
    def get(self):
        arguments = Resource.args()
        result = dao.getMessage(arguments.get('gName'), arguments.get('id'))
        if(result != None):
            return jsonify(Messages=result)
        return jsonify(Error="MESSAGE NOT FOUND"), 404
    
class MessageReactionHandler(Resource):
    arguments = Resource.args()
    
    def put(self):
        message = dao.getMessage(arguments.get('gName'), arguments.get('id'))
        if(message != None):
            message.setReaction(Resource.args().get('reaction'))
            return jsonify(Messages=message)
        else:
            return jsonify(Error="INTERNAL SERVER ERROR"), 500
    
class MessageSearchHandler(Resource):
    arguments = Resource.args()
    containsText = []
    def get(self):
        messages = dao.getAllMessages(Resource.args().get('gName'))
        for m in messages:
            if m[1] == arguments.get('text'):
                containsText.append(m)
        if(containsText):
            return jsonify(Messages=containsText)
        return jsonify(Result="TEXT NOT FOUND"), 204
    
class MessagePostHandler(Resource):
    arguments = Resource.args()
    def get(self):
        post = dao.postMessage(arguments.get('gName'), arguments.get('text'), 
                                 arguments.get('writerID'))
        if (post):
            return jsonify(Messages=post)
        return jsonify(Error="UNABLE TO POST MESSAGE"), 404
    Resource
    