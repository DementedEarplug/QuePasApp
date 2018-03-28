from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from handler.user_handler import UserByIdHandler, UserHandler, UserByNameHandler
from dao.group_chat_dao import ChatDAO
from handler.group_chat_handler import GroupHandler, GroupByIndexHandler, GroupByUserHandler
from dao.message_dao import MessagesDAO
from handler.message_handler import MessageHandler, MessageByIdHandler, MessageReactionHandler, MessageSearchHandler, MessagePostHandler

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return "The beginning"
    
#============================#
#          Chat API          #
#============================#

api.add_resource(GroupHandler, '/QuePasApp/groups')
api.add_resource(GroupByIndexHandler,'/QuePasApp/groups/<int:id>')
api.add_resource(GroupByUserHandler, '/QuePasApp/groups/user/<int:userID>')
#Try to follow this format ^^ (It's more compact and legible, and i believe it's easier too)

#============================#
#        Message API         #
#============================#

#Returns all messages available in the group
api.add_resource(MessageHandler, '/QuePasApp/groups/<string:gName>/messages')

#Returns a specific message by using its id
api.add_resource(MessageByIdHandler, '/QuePasApp/groups/<string:gName>/messages/<int:id>')

#Adds a reaction to the message that corresponds to the Id
api.add_resource(MessageReactionHandler, '/QuePasApp/groups/<string:gName>/messages/<int:id>')

#Searches for a message that contains the text specified
api.add_resource(MessageSearchHandler, '/QuePasApp/groups/<string:gName>/messages/<string:text>')

#Posts a new message into group
api.add_resource(MessagePostHandler, '/QuePasApp/groups/<string:gName>/messages/post')

#============================#
#         User API           #
#============================#

#Diplays all the users in a given group
api.add_resource(UserHandler, '/QuePasApp/users' )

#Searches users by given id
api.add_resource(UserByIdHandler, '/QuePasApp/users/<int:IdUser>')

#Searches user by a given First Name
api.add_resource(UserByNameHandler, '/QuePasApp/users/<string:uFirstName>')


if(__name__=='__main__'):
    app.run(debug = True, port = 8080)
    