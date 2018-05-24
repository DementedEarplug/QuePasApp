from flask import jsonify
import psycopg2
from config import db_config
from datetime import datetime

#Message Data Access object that retrieves data from the DB (currently hardcoded)
class MessagesDAO:
    #Hardcoded message data corresponding to one group chat is created
    def __init__(self):
        #maybe jsut add el url del DB directly?
        connection_url = "dbname=%s user=%s password=%s" % (db_config['dbname'],  db_config['user'], db_config['passwd'])
        self.conn = psycopg2._connect('postgres://rdoycbxokxgmsz:d9980f20415499517e3caacaa67ee00376d331677988af4b8c4887fc65235efc@ec2-75-101-142-91.compute-1.amazonaws.com:5432/d2o9j3bddfg00r')
    
    #All messages from all group chats are retrieved
    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = 'select * from messages'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    def likeMessage(self, userid, msgid):
        cursor = self.conn.cursor()
        query = "select count(messages.msgid), count(users.userid) from users, messages where users.userid = %s and messages.msgid = %s"
        cursor.execute(query, [userid, msgid])
        result = cursor.fetchone()
        if(result[0]>0 and result[1]>0):
            query = "select count(*) from likes where userid = %s and msgid = %s"
            cursor.execute(query, [userid, msgid])
            if(cursor.fetchone()[0]==0):
                query = "insert into likes (userid, msgid) values(%s, %s)"
                cursor.execute(query, [userid, msgid])
                self.conn.commit()
                return "Like Added to message", 201
            else:
                query = "delete from likes where userid = %s and msgid = %s"
                cursor.execute(query, [userid, msgid])
                self.conn.commit()
                return "Like removed from messages", 201
        else:
            return "User or message does not exist",404
    def dislikeMessage(self, userid, msgid):
        cursor = self.conn.cursor()
        query = "select count(messages.msgid), count(users.userid) from users, messages where users.userid = %s and messages.msgid = %s"
        cursor.execute(query, [userid, msgid])
        result = cursor.fetchone()
        if(result[0]>0 and result[1]>0):
            query = "select count(*) from dislikes where userid = %s and msgid = %s"
            cursor.execute(query, [userid, msgid])
            if(cursor.fetchone()[0]==0):
                query = "insert into dislikes (userid, msgid) values(%s, %s)"
                cursor.execute(query, [userid, msgid])
                self.conn.commit()
                return "Dislike Added to message", 201
            else:
                query = "delete from dislikes where userid = %s and msgid = %s"
                cursor.execute(query, [userid, msgid])
                self.conn.commit()
                return "Dislike removed from messages", 201
        else:
            return "User or message does not exist",404
        
    #All messages corresponding to a group chat are retrieved 
    def getGroupMessages(self, groupId):    #Maybe add the posibility of IDing groupd by both name and ID.
        cursor = self.conn.cursor()
        q1 = ' select msgid, content, username,'
        q2 = ' (select count(*) from likes where likes.msgId = messages.msgId) as likes,'
        q3 = ' (select count(*) from dislikes where dislikes.msgId = messages.msgId) as dislikes,'
        q4 = ' (select exists(select msgid from replies where replies.msgid = messages.msgid)) as IsReply,'
        q5 = ' (select case when exists(select msgid from replies where replies.msgid = messages.msgid)'
        q6 = ' then(select repliedtoid from replies where replies.msgid = messages.msgid) else null end) as repliesTo'
        q7 = ' from messages natural inner join users natural inner join groups where groupId = %s;'
        query = q1 + q2 + q3 + q4 + q5 + q6 + q7
        print(query)
        cursor.execute(query,(groupId,))
        result = cursor.fetchall()
        return result
    def sendMessage(self, authorId, groupId, content):
        cursor = self.conn.cursor()
        fulldate = datetime.now()
        postdate = str(fulldate).split(' ')[0]
        posttime = str(fulldate).split(' ')[1]
        query = "Insert into messages (userid, groupid, content, postdate, posttime) values(%s, %s, %s, %s, %s)"
        cursor.execute(query, [authorId, groupId, content, postdate, posttime])
        self.conn.commit()
        cursor.execute("Select msgid from messages where postdate = %s and posttime = %s", [postdate, posttime])
        return cursor.fetchone()[0]
    def sendReply(self, fromId, toId):
        cursor = self.conn.cursor()
        query = "Insert into replies(repliedtoid, msgid) values(%s, %s)"
        cursor.execute(query, [toId, fromId])
        self.conn.commit()
    def addHashtag(self, msgid, hashtag):
        query = "insert into hashtags (msgid, hashtagcontent) values(%s, %s)"
        cursor = self.conn.cursor()
        cursor.execute(query,[msgid, hashtag])
        self.conn.commit()

        
    #A message that corresponds to the given ID is searched in the corresponding group chat
    def getMessage(self, id):
        cursor = self.conn.cursor()
        query = 'Select * from messages where msgid = %s'
        cursor.execute(query,[id])
        result = cursor.fetchone()
        print(result)
        res = []
        for r in result:
            res.append(str(r))
        print(res)
        if result:
            return {'Message': res}
        else: 
            return None
    
    #A message is posted into the corresponding group chat using the latest message id,
    #a given content, writerID, groupID, and current time and date
    def postMessage(self, gName, content, uID):
        print("Before For")
        for g in self.groupNames:
            print(g)
            if g == gName:
                print("Group Name: " + g)
                group = self.data[self.groupIds[g]]
                print(group)
                groupSize = len(group)
                print("Group Size: " + str(groupSize))
                lastId = group[groupSize - 1]['id']
                print("Last Id: " + str(lastId))
                m = Message(lastId + 1, content, uID, self.groupIds[g], time.strftime("%X"), time.strftime("%x")).toDict()
                group.append(m)
                return m
        return None

