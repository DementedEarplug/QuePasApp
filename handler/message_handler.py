from flask_restful import Resource
from flask import jsonify
from flask_restful import reqparse
from dao.message_dao import MessagesDAO
#from test.support import resource

#Construct DAO Instance
dao = MessagesDAO()

#Contains implementation related to all message handling operations of the application

class MessageHandler(Resource):
    def get(self, gName):
        result = dao.getAllMessages(gName)
        if (result != None):
            return jsonify(Messages=result)
        return jsonify(Error="MESSAGES NOT FOUND"), 404
    
class MessageByIdHandler(Resource):
    def get(self, gName, id):
        result = dao.getMessage(gName, id)
        if(result != None):
            return jsonify(Messages=result)
        return jsonify(Error="MESSAGE NOT FOUND"), 404
    
class MessageReactionHandler(Resource):
    #def get (get reactions for messages)
    def put(self, gName, id):
        message = dao.getMessage(gName, id)
        if(message != None):
            parser = reqparse.RequestParser()
            parser.add_argument('reaction', type=str, location = 'args')
            args = parser.parse_args(strict=True)
            message['reaction'] = args['reaction']
            return jsonify(Messages=message)
        else:
            return jsonify(Error="INTERNAL SERVER ERROR"), 500
    
class MessageSearchHandler(Resource):
    
    def get(self, gName, text):
        containsText = []
        messages = dao.getAllMessages(gName)
        if(messages != None):
            for m in messages:
                if m['content'] == text:
                    containsText.append(m)
            if(containsText):
                return jsonify(Messages=containsText)
            return jsonify(Error="TEXT NOT FOUND"), 204
        return jsonify(Error="INTERNAL SERVER ERROR"), 500
    
class MessagePostHandler(Resource):
    def post(self, gName):
        parser = reqparse.RequestParser()
        parser.add_argument('text', type=str, location = 'args')
        parser.add_argument('writerID', type=int, location = 'args')
        args = parser.parse_args(strict=True)
        post = dao.postMessage(gName, args['text'], args['writerID'])
        if (post != None):
            return jsonify(Messages=post)
        return jsonify(Error="UNABLE TO POST MESSAGE"), 404
##RepliesHandler
##get message id, check that id on replies table, return reply object (replyID, messageID, respondsToID)