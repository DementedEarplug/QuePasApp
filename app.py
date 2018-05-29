from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from dao.group_chat_dao import ChatDAO
from dao.message_dao import MessagesDAO
from flask_cors import CORS, cross_origin
from handler import message_handler as mHand, user_handler as uHand, group_chat_handler as gHand

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/')
def home():
    return "The beginning"

#============================#
#          Chat API          #
#============================#
#returns every group
api.add_resource(gHand.GroupHandler, '/QuePasApp/groups/') #done

api.add_resource(gHand.CreateGroupHandler, '/QuePasApp/groups/new')

api.add_resource(gHand.RemoveUser,  '/QuePasApp/groups/<int:groupId>/removeUser/<int:userId>')

#return a single group
api.add_resource(gHand.GroupByIndexHandler,'/QuePasApp/groups/<int:groupId>/') 

#returns every group where user is owner
api.add_resource(gHand.GroupByOwnerHandler, '/QuePasApp/groups/user/<int:userId>/') 

#returns the owner of a group
api.add_resource(gHand.GroupOwnerHandler, '/QuePasApp/groups/<int:groupId>/owner/')

#returns every groups where user is participant
api.add_resource(gHand.UserGroupsHandler, '/QuePasApp/users/<int:userId>/groups/') 

api.add_resource(gHand.JoinGroupHandler, '/QuePasApp/groups/<int:groupId>/addUser/<int:userId>')


#============================#
#        Message API         #
#============================#

#Returns all messages
api.add_resource(mHand.MessageHandler, '/QuePasApp/messages/all')

api.add_resource(mHand.SendMessageHandler, '/QuePasApp/messages/send')

api.add_resource(mHand.sendReplyHandler, '/QuePasApp/messages/sendReply')

#Returns count of all messages
api.add_resource(mHand.MessageCountHandler, '/QuePasApp/messages/count/')

#Returns all messages available in the group
api.add_resource(mHand.GroupMessageHandler, '/QuePasApp/groups/<int:groupId>/messages')

#Returns a specific message by using its id
api.add_resource(mHand.MessageByIdHandler, '/QuePasApp/messages/<int:id>/')

#Returns list of users that like a specific message by using its id
api.add_resource(mHand.MessageLikesHandler, '/QuePasApp/messages/<int:msgId>/likes')

api.add_resource(mHand.AddLikeHandler, '/QuePasApp/messages/sendLike')

api.add_resource(mHand.AddDislikeHandler, '/QuePasApp/messages/sendDislike')

#Returns list of users that dislike a specific message by using its id
api.add_resource(mHand.MessageDislikesHandler, '/QuePasApp/messages/<int:msgId>/dislikes')

#Returns the count of likes in a specific message by using its id
api.add_resource(mHand.MessageLikeCountHandler, '/QuePasApp/messages/<int:msgId>/likeCount')

#Returns the count of dislikes in a specific message by using its id
api.add_resource(mHand.MessageDislikeCountHandler, '/QuePasApp/messages/<int:msgId>/dislikeCount')

#Adds a reaction to the message that corresponds to the Id
api.add_resource(mHand.MessageReactionHandler, '/QuePasApp/groups/<string:gName>/messages/<int:id>')

#Searches for a message that contains the text specified
api.add_resource(mHand.MessageSearchHandler, '/QuePasApp/groups/<int:groupId>/messages/search')

#Gets message count in total 


#============================#
#         User API           #
#============================#

#Diplays all the users in a given group
api.add_resource(uHand.UserHandler, '/QuePasApp/users/' )

#resgisters a new user form the REST API
api.add_resource(uHand.AddUserHandler, '/QuePasApp/users/new')

#Searches users by given id
api.add_resource(uHand.UserByIdHandler, '/QuePasApp/users/<int:userId>/')

#Searches user by a given First Name
api.add_resource(uHand.UserByNameHandler, '/QuePasApp/users/firstname/<string:uFirstName>/')

#Searches a user by a given Last Name
api.add_resource(uHand.UserByLastNameHandler, '/QuePasApp/users/lastname/<string:uLastname>/')

#Searches a user by a given username
api.add_resource(uHand.GetByUsernameHandler,'/QuePasApp/users/username/<string:username>/')

#Displays contact list of a user with a given ID
api.add_resource(uHand.ContactListHandler, '/QuePasApp/users/<int:ownerId>/contactlist')

# Displays every participants of a group
api.add_resource(uHand.UsersInGroupHandler, '/QuePasApp/groups/<int:groupId>/participants/')

# User login endpoint
api.add_resource(uHand.UserLoginHandler, '/QuePasApp/login')


#============================#
#       Dashboard API        #
#============================#

#Data to generate Trending Hashtag
api.add_resource(mHand.TrendingHashtagHandler, '/QuePasApp/DashBoard/trending' )

#Data to generate msg per day chart
api.add_resource(mHand.MsgsPerDayHandler, '/QuePasApp/DashBoard/messeagesPerDay' )

# #Data to generate replies per day chart
api.add_resource(mHand.RepliesPerDayHandler, '/QuePasApp/DashBoard/repliesPerDay' )

# #Data to generate likes per day chart
api.add_resource(mHand.LikesPerDayHandler, '/QuePasApp/DashBoard/likesPerDay' )

# #Data to generate dislikes per day chart
api.add_resource(mHand.DislikesPerDayHandler, '/QuePasApp/DashBoard/dislikesPerDay' )

#Data to generate active users per day
api.add_resource(uHand.ActiveUsersHandler, '/QuePasApp/DashBoard/ActiveUsersPerDay' )





if(__name__=='__main__'):
    app.run(debug = True, host="192.168.0.3", port = 8000)
    #app.run(debug = True, port = 8000)
    
