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

    def getMsgsPerDay(self):
        cursor = self.conn.cursor()
        query = '''select messages.postdate, count(*)
        from messages
        group by messages.postdate;'''
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getTrending(self):
        cursor = self.conn.cursor()
        query = '''select hashtagcontent, count(*) as count
        from hashtags
        group by hashtagcontent
        order by count desc
        limit 10;'''
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getLikesPerDay(self):
        cursor = self.conn.cursor()
        query = '''select postdate, count(*)
        from likes 
        group by postdate;'''
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDislikesPerDay(self):
        cursor = self.conn.cursor()
        query = '''select postdate, count(*)
        from dislikes 
        group by postdate;'''
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getRepliesPerDay(self):
        cursor = self.conn.cursor()
        query = '''select messages.postdate, count(*)
        from messages natural  inner join  replies
        where messages.msgid = replies.msgid
        group by messages.postdate'''
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
                fulldate = datetime.now()
                postdate = str(fulldate).split(' ')[0]
                posttime = str(fulldate).split(' ')[1]
                query = "insert into likes (userid, msgid, posttime, postdate) values(%s, %s, %s, %s)"
                cursor.execute(query, [userid, msgid, posttime, postdate])
                self.conn.commit()
                return "Like Added to message"
            else:
                query = "delete from likes where userid = %s and msgid = %s"
                cursor.execute(query, [userid, msgid])
                self.conn.commit()
                return "Like removed from messages"
        else:
            return "User or message does not exist"
    
    def dislikeMessage(self, userid, msgid):
        cursor = self.conn.cursor()
        query = "select count(messages.msgid), count(users.userid) from users, messages where users.userid = %s and messages.msgid = %s"
        cursor.execute(query, [userid, msgid])
        result = cursor.fetchone()
        if(result[0]>0 and result[1]>0):
            query = "select count(*) from dislikes where userid = %s and msgid = %s"
            cursor.execute(query, [userid, msgid])
            if(cursor.fetchone()[0]==0):
                fulldate = datetime.now()
                postdate = str(fulldate).split(' ')[0]
                posttime = str(fulldate).split(' ')[1]
                query = "insert into dislikes (userid, msgid, posttime, postdate) values(%s, %s, %s, %s)"
                cursor.execute(query, [userid, msgid, posttime, postdate])
                self.conn.commit()
                return "Dislike Added to message"
            else:
                query = "delete from dislikes where userid = %s and msgid = %s"
                cursor.execute(query, [userid, msgid])
                self.conn.commit()
                return "Dislike removed from messages"
        else:
            return "User or message does not exist"
        
    #All messages corresponding to a group chat are retrieved 
    def getGroupMessages(self, groupId):    #Maybe add the posibility of IDing groupd by both name and ID.
        cursor = self.conn.cursor()
        q1 = ' select msgid, content, username,'
        q2 = ' (select count(*) from likes where likes.msgId = messages.msgId) as likes,'
        q3 = ' (select count(*) from dislikes where dislikes.msgId = messages.msgId) as dislikes,'
        q4 = ' (select exists(select msgid from replies where replies.msgid = messages.msgid)) as IsReply,'
        q5 = ' (select case when exists(select msgid from replies where replies.msgid = messages.msgid)'
        q6 = ' then(select repliedtoid from replies where replies.msgid = messages.msgid) else null end) as repliesTo,'
        q7 = ' postdate, posttime'
        q8 = ' from messages natural inner join users natural inner join groups where groupId = %s;'
        query = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8
        cursor.execute(query,(groupId,))
        result = cursor.fetchall()
        return result
    
    def searchHashTagGroupMessages(self, groupId, hashtag):    #Maybe add the posibility of IDing groupd by both name and ID.
        cursor = self.conn.cursor()
        q1 = ' select msgid, content, username,'
        q2 = ' (select count(*) from likes where likes.msgId = messages.msgId) as likes,'
        q3 = ' (select count(*) from dislikes where dislikes.msgId = messages.msgId) as dislikes,'
        q4 = ' (select exists(select msgid from replies where replies.msgid = messages.msgid)) as IsReply,'
        q5 = ' (select case when exists(select msgid from replies where replies.msgid = messages.msgid)'
        q6 = ' then(select repliedtoid from replies where replies.msgid = messages.msgid) else null end) as repliesTo,'
        q7 = ' postdate, posttime'
        q8 = ' from messages natural inner join users natural inner join groups natural inner join hashtags where groupId = %s and hashtagcontent = %s;'
        query = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8
        print(query)
        cursor.execute(query,(groupId, hashtag,))
        result = cursor.fetchall()
        return result

    def sendMessage(self, authorId, groupId, content):
        cursor = self.conn.cursor()
        fulldate = datetime.now()
        postdate = str(fulldate).split(' ')[0]
        posttime = str(fulldate).split(' ')[1]
        check = "select * from participants where userid = %s and groupid = %s"
        cursor.execute(check, [authorId, groupId])
        checkResult = cursor.fetchone()
        if(checkResult):
            query = "Insert into messages (userid, groupid, content, postdate, posttime) values(%s, %s, %s, %s, %s) returning *"
            cursor.execute(query, [authorId, groupId, content, postdate, posttime])
            self.conn.commit()
            message = cursor.fetchone()
            q1 = ' select msgid, content, username, '
            q2 = ' (select count(*) from likes where likes.msgId = messages.msgId) as likes,'
            q3 = ' (select count(*) from dislikes where dislikes.msgId = messages.msgId) as dislikes,'
            q4 = ' (select exists(select msgid from replies where replies.msgid = messages.msgid)) as IsReply,'
            q5 = ' (select case when exists(select msgid from replies where replies.msgid = messages.msgid)'
            q6 = ' then(select repliedtoid from replies where replies.msgid = messages.msgid) else null end) as repliesTo,'
            q7 = ' postdate, posttime'
            q8 = ' from messages natural inner join users natural inner join groups where groupId = %s and msgId = %s;'
            query = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8
            cursor.execute(query, [groupId, message[0]])
            completeMessage = cursor.fetchone()
            return {"Message":completeMessage}
        else:
            return {"Error":"User is not member of group"}

    def sendReply(self, message, toId):
        cursor = self.conn.cursor()
        query = "Insert into replies(repliedtoid, msgid) values(%s, %s)"
        cursor.execute(query, [toId, message])
        self.conn.commit()
    def getNumberOfMessages(self):
        query = "Select count(*) from messages"
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchone()[0]

    def addHashtag(self, message, hashtag):
        query = "insert into hashtags (msgid, hashtagcontent) values(%s, %s)"
        cursor = self.conn.cursor()
        cursor.execute(query,[message, hashtag])
        self.conn.commit()

        
    #A message that corresponds to the given ID is searched in the corresponding group chat
    def getMessage(self, id):
        cursor = self.conn.cursor()
        query = 'Select * from messages where msgid = %s'
        cursor.execute(query,[id])
        result = cursor.fetchone()
        res = []
        if result:
            for r in result:
                res.append(str(r))
            return {'Message': res}
        else: 
            return None
