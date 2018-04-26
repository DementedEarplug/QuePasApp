from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from handler.user_handler import UserByIdHandler, UserHandler, UserByNameHandler, UserByLastNameHandler, GetByUsernameHandler, UsernameHandler, ContactListHandler
from dao.group_chat_dao import ChatDAO
from handler.group_chat_handler import GroupHandler, GroupByIndexHandler, GroupByOwnerHandler, GroupParticipantsHandler, GroupOwnerHandler, UserGroupsHander
from dao.message_dao import MessagesDAO
from handler.message_handler import MessageHandler, MessageByIdHandler, MessageReactionHandler, MessageSearchHandler, MessagePostHandler, GroupMessageHandler, MessageCountHandler

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return "The beginning"

#============================#
#          Chat API          #
#============================#
#returns every group
api.add_resource(GroupHandler, '/QuePasApp/groups/') #done #done

#return a single group
api.add_resource(GroupByIndexHandler,'/QuePasApp/groups/<int:id>/') #done #done

#returns every participants of a group
api.add_resource(GroupParticipantsHandler, '/QuePasApp/groups/<int:groupID>/participants/') #done #done

#returns every group where user is owner
api.add_resource(GroupByOwnerHandler, '/QuePasApp/groups/user/<int:userID>/') #done #done

#returns the owner of a group
api.add_resource(GroupOwnerHandler, '/QuePasApp/groups/<int:groupID>/owner/') #done #done

#returns every groups where user is participant
api.add_resource(UserGroupsHander, '/QuePasApp/users/<int:userID>/groups/') #done


#============================#
#        Message API         #
#============================#

#Returns all messages
api.add_resource(MessageHandler, '/QuePasApp/groups/messages/')

#Returns count of all messages
api.add_resource(MessageCountHandler, '/QuePasApp/groups/messages/count/')

#Returns all messages available in the group
api.add_resource(GroupMessageHandler, '/QuePasApp/groups/<string:gName>/messages')

#Returns a specific message by using its id
api.add_resource(MessageByIdHandler, '/QuePasApp/groups/<string:gName>/messages/<int:id>/')

#Adds a reaction to the message that corresponds to the Id
api.add_resource(MessageReactionHandler, '/QuePasApp/groups/<string:gName>/messages/<int:id>')

#Searches for a message that contains the text specified
api.add_resource(MessageSearchHandler, '/QuePasApp/groups/<string:gName>/messages/<string:text>/')

#Posts a new message into group (old implementation)
#api.add_resource(MessagePostHandler, '/QuePasApp/groups/<string:gName>/messages/post')

#Gets message count in total 


#============================#
#         User API           #
#============================#

#Diplays all the users in a given group
api.add_resource(UserHandler, '/QuePasApp/users/' )

#Return the usernames of all available users
api.add_resource(UsernameHandler, '/QuePasApp/users/username/' )

#Searches users by given id
api.add_resource(UserByIdHandler, '/QuePasApp/users/<int:userId>/')

#Searches user by a given First Name
api.add_resource(UserByNameHandler, '/QuePasApp/users/firstname/<string:uFirstName>/')

#Searches a user by a given Last Name
api.add_resource(UserByLastNameHandler, '/QuePasApp/users/lastname/<string:uLastname>/')

#Searches a user by a given username
api.add_resource(GetByUsernameHandler,'/QuePasApp/users/username/<string:username>/')

#Displays contact list of a user with a given ID
api.add_resource(ContactListHandler, '/QuePasApp/users/<int:userId>/contactlist')


if(__name__=='__main__'):
    app.run(debug = True, port = 8080)
    