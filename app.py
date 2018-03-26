from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from handler.user_handler import UserHandler
from dao.group_chat_dao import ChatDAO
from handler.group_chat_handler import GroupHandler, GroupByIndexHandler, GroupByUserHandler

app = Flask(__name__)
api = Api(app)


#chat api 
api.add_resource(GroupHandler, '/api/groups')
api.add_resource(GroupByIndexHandler,'/api/groups/<int:id>')
api.add_resource(GroupByUserHandler, '/api/groups/user/<int:userID>')
#Try to follow this format ^^ (It's more compact and legible, and i believe it's easier too)

@app.route('/')
def home():
    return "The beginning"

@app.route('/api/users')
def users():
    if request.args:
        return UserHandler().searchUserByName(request.args)
    else:
        handler = UserHandler()
        return handler.getAllUsers()

@app.route('/api/users/<int:IdUser>')
def getUserById(IdUser):
    handler = UserHandler()
    return handler.getUserbyId(IdUser)


if(__name__=='__main__'):
    app.run(debug = True, port = 8080)
    