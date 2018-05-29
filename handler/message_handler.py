from flask_restful import Resource
from flask import Response, jsonify, request
from flask_restful import reqparse
from dao.message_dao import MessagesDAO
from dao.reactions_dao import ReactionsDAO
from dao.user_dao import UserDAO
import json

#Construct DAO Instance
def mapAllMessages(row):
    mappedMsg = {}
    mappedMsg['msgId'] = row[0]
    mappedMsg['content'] = row[1]
    mappedMsg['userid'] = row[2]
    mappedMsg['groupid'] = row[3]
    # mappedMsg['dislikes'] = row[4]
    # mappedMsg['isReply'] = row[5]
    # mappedMsg['repliesTo'] = row[6]
    mappedMsg['postDate'] = str(row[4])
    mappedMsg['postTime'] = str(row[5])
    return mappedMsg

def mapToDict(row):
    mappedMsg = {}
    mappedMsg['msgId'] = row[0]
    mappedMsg['content'] = row[1]
    mappedMsg['username'] = row[2]
    mappedMsg['likes'] = row[3]
    mappedMsg['dislikes'] = row[4]
    mappedMsg['isReply'] = row[5]
    mappedMsg['repliesTo'] = row[6]
    mappedMsg['postDate'] = str(row[7])
    mappedMsg['postTime'] = str(row[8])
    return mappedMsg

def mapMsgPerDay(row):
    mappedMsg = {}
    mappedMsg['postdate'] = row[0]
    mappedMsg['count'] = row[1]
    
    return mappedMsg

def mapHashTag(row):
    mappedMsg = {}
    mappedMsg['hashtagcontent'] = row[0]
    mappedMsg['count'] = row[1]
    
    return mappedMsg

def mapLikesToDiCt(row):
    mappedLikes = {}
    mappedLikes['likeId']= row[0]
    mappedLikes['userId']= row[1]
    mappedLikes['msgId']= row[2]
    return mappedLikes

def mapDislikesToDiCt(row):
    mappedDislikes = {}
    mappedDislikes['dislikeId']= row[0]
    mappedDislikes['userId']= row[1]
    mappedDislikes['msgId']= row[2]
    return mappedDislikes


#Function to map the result of a query into a dictionary.
def mapUserToDict(row):
    mappedUser = {}
    mappedUser['username'] = row[0]
    return mappedUser

#Contains implementation related to all message handling operations of the application

class MessageHandler(Resource):
    def get(self):
        dao = MessagesDAO()
        msgList = dao.getAllMessages()
        resultList = []
        for row in msgList:
            result = mapAllMessages(row)
            resultList.append(result)
        if (len(resultList)!=0):
            return jsonify(Messages= resultList)
        else:
            return {"Eror", "Messages Not Found"}, 404

class MsgsPerDayHandler(Resource):
    def get(self):
        dao = MessagesDAO()
        msgList = dao.getMsgsPerDay()
        mesgsPerDay = []
        for row in msgList:
            result = mapMsgPerDay(row)
            mesgsPerDay.append(result)
        if (len(mesgsPerDay)!=0):
            return jsonify(MessagesPerDay= mesgsPerDay)
        else:
            return {"Error":"Not Found"}, 404

class RepliesPerDayHandler(Resource):
    def get(self):
        dao = MessagesDAO()
        msgList = dao.getRepliesPerDay()
        repliesPerDay = []
        for row in msgList:
            result = mapMsgPerDay(row)
            repliesPerDay.append(result)
        if (len(repliesPerDay)!=0):
            return jsonify(RepliesPerDay= repliesPerDay)
        else:
            return {"Error":"Not Found"}, 404

class LikesPerDayHandler(Resource):
    def get(self):
        dao = MessagesDAO()
        likeList = dao.getLikesPerDay()
        likessPerDay = []
        for row in likeList:
            result = mapMsgPerDay(row)
            likessPerDay.append(result)
        if (len(likessPerDay)!=0):
            return jsonify(LikesPerDay= likessPerDay)
        else:
            return {"Error":"Not Found"}, 404

class DislikesPerDayHandler(Resource):
    def get(self):
        dao = MessagesDAO()
        dislikeList = dao.getDislikesPerDay()
        dislikessPerDay = []
        for row in dislikeList:
            result = mapMsgPerDay(row)
            dislikessPerDay.append(result)
        if (len(dislikessPerDay)!=0):
            return jsonify(DislikesPerDay= dislikessPerDay)
        else:
            return {"Error":"Not Found"}, 404

class TrendingHashtagHandler(Resource):
    def get(self):
        dao = MessagesDAO()
        hashTags = dao.getTrending()
        trending = []
        for row in hashTags:
            result = mapHashTag(row)
            trending.append(result)
        if (len(trending)!=0):
            return jsonify(Trending= trending)
        else:
            return {"Error":"Not Found"}, 404

class SendMessageHandler(Resource):
    def post(self):
       dao = MessagesDAO()
       msg = dao.sendMessage(request.form['authorId'], request.form['groupId'], request.form['content'])
       if(msg.keys().__contains__("Message")):
           content = request.form['content']
           hashtagCheck = str(content).split(' ')
           for part in hashtagCheck:
               if(part[0]=='#'):
                   dao.addHashtag(msg["Message"][0], part)
           msgDict = mapToDict(msg["Message"])
           return {"Message":msgDict},201
       elif(msg.keys().__contains__("Error")):
            return msg,403
       return {"Internal Server Error" : "Message not sent"}, 500

class SendReplyHandler(Resource):

    def post(self):
        dao = MessagesDAO()
        msg = dao.sendMessage(request.form['authorId'], request.form['groupId'], request.form['content'])
        if(msg.keys().__contains__("Message")):
            content = request.form['content']
            hashtagCheck = str(content).split(' ')
            for part in hashtagCheck:
               if(part[0]=='#'):
                    dao.addHashtag(msg["Message"][0], part)
            msgDict = mapToDict(msg["Message"])
            dao.sendReply(msgDict['msgId'], request.form['msgid'])
            return {"Message":msgDict},201
        elif(msg.keys().__contains__("Error")):
            return msg,403
        return {"Internal Server Error" : "Message not sent"}, 500

        
        
    
class MessageLikesHandler(Resource):
    # Returns the users who like a message with a given ID.
    def get(self, msgId):
        rDao = ReactionsDAO()
        userList = rDao.getLikeList(msgId)
        resultList= []
        for row in userList:
            result = mapUserToDict(row)
            resultList.append(result)
        if (len(resultList)!=0):
            return jsonify(Users= resultList)
        else:
            return {"Error":"NOT FOUND"},404

class AddLikeHandler(Resource):
    def post(self):
        userid = request.form['userid']
        msgid = request.form['msgid']
        dao = MessagesDAO()
        result = dao.likeMessage(userid, msgid)
        return jsonify(Result=result)
class AddDislikeHandler(Resource):
    def post(self):
        userid = request.form['userid']
        msgid = request.form['msgid']
        dao = MessagesDAO()
        result = dao.dislikeMessage(userid, msgid)
        return jsonify(Result=result)
        

class MessageDislikesHandler(Resource):
    # Returns the users who like a message with a given ID.
    def get(self, msgId):

        rDao = ReactionsDAO()
        userList = rDao.getDislikeList(msgId)
        resultList= []
        for row in userList:
            result = mapUserToDict(row)
            resultList.append(result)
        if (len(resultList)!=0):
            return jsonify(Users= resultList)
        else:
            return {"Error":"NOT FOUND"}, 404

class MessageLikeCountHandler(Resource):
    def get(self,msgId):
        rDao = ReactionsDAO()
        count = rDao.getMsgLikesCount(msgId)
        if not count:
            return {"Error":"Message Not Found"},404
        else:
            return jsonify(Likes= count)

class MessageDislikeCountHandler(Resource):
    def get(self,msgId):
        rDao = ReactionsDAO()
        count = rDao.getMsgDislikesCount(msgId)
        if not count:
            return jsonify(Error="Not Found"),404
        else:
            return jsonify(Dislikes= count)          

#General Message Handler that returns all messages in the group chat
class GroupMessageHandler(Resource):
    def get(self, groupId):
        dao = MessagesDAO()
        msgList = dao.getGroupMessages(groupId)
        resultList = []
        for row in msgList:
            result = mapToDict(row)
            resultList.append(result)
        if (len(resultList)!=0):
            return {"Messages": resultList}
        else:
            return {"Error":"Group Messages Not Found"}, 404

    def post(self, gName):
        dao = MessagesDAO()
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
    def get(self,id):
        dao = MessagesDAO()
        result = dao.getMessage(id) #Gets message that matches message id
        if(result):
            return jsonify(result) #If not null returns the corresponding message
        return {'Error' : "MESSAGE NOT FOUND"}, 404
        
#This handler will change the reaction status of the message 
#corresponding to the given id in the given group
class MessageReactionHandler(Resource):
    #def get (get reactions for messages)
    def put(self, gName, id):
        dao = MessagesDAO()
        message = dao.getMessage(gName, id)
        if(message):
            parser = reqparse.RequestParser()
            parser.add_argument('reaction', type=str, location = 'args')
            args = parser.parse_args(strict=True)
            message['reactions'].append(args['reaction'])
            return jsonify(Messages=message) #Message with new reaction is returned
        return {'Error' : "INTERNAL SERVER ERROR"}, 500

# #Text searches in a group chat's messages are performed
# class MessageSearchHandler(Resource):
#     def get(self, groupId):
#         containsText = []
#         text = request.args.get("text")
#         dao = MessagesDAO()
#         messages = dao.getGroupMessages(groupId)
#         resultList = []
#         for row in messages: 
#             resultList.append(mapToDict(row))
#         if(resultList):
#             for m in resultList:
#                 if text in m['content']:
#                     containsText.append(m)
#             if(containsText):
#                 return jsonify(Messages=containsText) #Message that contains text is returned
#             return {'Result' : "TEXT NOT FOUND"}, 204 #Text not found
#         return {'Error' : "INTERNAL SERVER ERROR"}, 500 
    
#Text searches in a group chat's messages are performed
class MessageSearchHandler(Resource):
    def get(self, groupId):
        containsText = []
        hashtag = "#" + request.args.get("hashtag")
        print(hashtag)
        dao = MessagesDAO()
        messages = dao.searchHashTagGroupMessages(groupId, hashtag)
        resultList = []
        for row in messages: 
            resultList.append(mapToDict(row))
        if(resultList):
            return jsonify(Messages=resultList) #Message that contains text is returned
        return {'Messages' : "Hashtag not found"}, 404 #Text not found

#Messages are posted in the corresponding group chat considering 
#the content, writerID, and current time and date
class MessagePostHandler(Resource):
    def post(self, gName):
        dao = MessagesDAO()
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
        dao = MessagesDAO()
        result = dao.getNumberOfMessages()
        return result
##RepliesHandler
##get message id, check that id on replies table, return reply object (replyID, messageID, respondsToID)
