from flask_restful import Resource
from flask import Response, jsonify
from flask_restful import reqparse
from dao.message_dao import MessagesDAO

#Construct DAO Instance
dao = MessagesDAO()

#Contains implementation related to all message handling operations of the application

class MessageHandler(Resource):
    def get(self):
        result = dao.getAllMessages()
        if(result):
            return jsonify(Messages=result)
        return {'Error' : "INTERNAL SERVER ERROR"}, 500
    
#General Message Handler that returns all messages in the group chat
class GroupMessageHandler(Resource):
    def get(self, gName):
        result = dao.getGroupMessages(gName) #Gets all messages with DAO
        if (result):
            return jsonify(Messages=result) #If not null returns all of the group chat messages
        return {'Error' : "MESSAGES NOT FOUND"}, 404
    def post(self, gName):
        parser = reqparse.RequestParser()
        parser.add_argument('text', type=str, location = 'json')
        parser.add_argument('writerId', type=int, location = 'json')
        args = parser.parse_args(strict=True) #Arguments in query are stored in args
        post = dao.postMessage(gName, args['text'], args['writerId']) #Creates message
        if (post):
            return jsonify(Messages=post)
        return {'Error' : "UNABLE TO POST MESSAGE"}, 500
    
#Specific Message Handler that returns messages that corresponds 
#to the given id in the current group chat
class MessageByIdHandler(Resource):
    def get(self, gName, id):
        result = dao.getMessage(gName, id) #Gets message that matches message id
        if(result):
            return jsonify(Messages=result) #If not null returns the corresponding message
        return {'Error' : "MESSAGE NOT FOUND"}, 404
        
#This handler will change the reaction status of the message 
#corresponding to the given id in the given group
class MessageReactionHandler(Resource):
    #def get (get reactions for messages)
    def put(self, gName, id):
        message = dao.getMessage(gName, id)
        if(message):
            parser = reqparse.RequestParser()
            parser.add_argument('reaction', type=str, location = 'args')
            args = parser.parse_args(strict=True)
            message['reactions'].append(args['reaction'])
            return jsonify(Messages=message) #Message with new reaction is returned
        return {'Error' : "INTERNAL SERVER ERROR"}, 500

#Text searches in a group chat's messages are performed
class MessageSearchHandler(Resource):
    def get(self, gName, text):
        containsText = []
        messages = dao.getGroupMessages(gName)
        if(messages):
            for m in messages:
                if text in m['content']:
                    containsText.append(m)
            if(containsText):
                return jsonify(Messages=containsText) #Message that contains text is returned
            return {'Result' : "TEXT NOT FOUND"}, 204 #Text not found
        return {'Error' : "INTERNAL SERVER ERROR"}, 500 

#Messages are posted in the corresponding group chat considering 
#the content, writerID, and current time and date
class MessagePostHandler(Resource):
    def post(self, gName):
        parser = reqparse.RequestParser()
        parser.add_argument('text', type=str, location = 'json')
        parser.add_argument('writerId', type=int, location = 'json')
        args = parser.parse_args(strict=True) #Arguments in query are stored in args
        post = dao.postMessage(gName, args['text'], args['writerId']) #Creates message
        if (post):
            return jsonify(Messages=post)
        return {'Error' : "UNABLE TO POST MESSAGE"}, 500

class MessageCountHandler(Resource):
    def get(self):
        result = dao.getAllMessages()
        if(result):
            count = 0
            for g in result:
                for m in g:
                    count = count + 1
            return jsonify(Count=count)
        return {'Error' : "INTERNAL SERVER ERROR"}, 500
##RepliesHandler
##get message id, check that id on replies table, return reply object (replyID, messageID, respondsToID)
