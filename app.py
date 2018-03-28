from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from handler.user_handler import UserByIdHandler, UserHandler, UserByNameHandler, UserByLastNameHandler, GetByUsernameHandler, UsernameHandler
from dao.group_chat_dao import ChatDAO
from handler.group_chat_handler import GroupHandler, GroupByIndexHandler, GroupByUserHandler, GroupParticipantsHandler, GroupOwnerHandler
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

api.add_resource(GroupParticipantsHandler, '/QuePasApp/groups/<int:groupID>/participants')

api.add_resource(GroupByUserHandler, '/QuePasApp/groups/user/<int:userID>')

api.add_resource(GroupOwnerHandler, '/QuePasApp/groups/<int:groupID>/owner')


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

@app.route('/')
def home():
    #Future implementation will contain the Dashboard
    return "The beginning"

#============================#
#         User API           #
#============================#

#Diplays all the users in a given group
api.add_resource(UserHandler, '/QuePasApp/users' )

#Return the usernames of all available users
api.add_resource(UsernameHandler, '/QuePasApp/users/username/' )

#Searches users by given id
api.add_resource(UserByIdHandler, '/QuePasApp/users/<int:IdUser>')

#Searches user by a given First Name
api.add_resource(UserByNameHandler, '/QuePasApp/users/firstname/<string:uFirstName>')

#Searches a user by a given Last Name
api.add_resource(UserByLastNameHandler, '/QuePasApp/users/lastname/<string:uLastname>')

#Searches a user by a given username
api.add_resource(GetByUsernameHandler,'/QuePasApp/users/username/<string:username>')




if(__name__=='__main__'):
    app.run(debug = True, port = 8080)
    