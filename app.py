from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from handler.user_handler import UserHandler
from dao.group_chat_dao import ChatDAO
from handler.group_chat_handler import GroupHandler, GroupByIndexHandler, GroupByUserHandler

app = Flask(__name__)
api = Api(app)

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

@app.route('/')
def home():
    return "The beginning"

@app.route('/QuePasApp/users')
def users():
    if request.args:
        return UserHandler().searchUserByName(request.args)
    else:
        handler = UserHandler()
        return handler.getAllUsers()

@app.route('/QuePasApp/users/<int:IdUser>')
def getUserById(IdUser):
    handler = UserHandler()
    return handler.getUserbyId(IdUser)


if(__name__=='__main__'):
    app.run(debug = True, port = 8080)
    