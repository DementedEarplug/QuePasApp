from flask import jsonify
import psycopg2
from config import db_config

#Message Data Access object that retrieves data from the DB (currently hardcoded)
class MessagesDAO:
    #Hardcoded message data corresponding to one group chat is created
    def __init__(self):
        #maybe jsut add el url del DB directly?
        connection_url = "dbname=%s user=%s password=%s" % (db_config['dbname'],  db_config['user'], db_config['passwd'])
        self.conn = psycopg2._connect('postgres://ekabibbfjhmljk:ea67f5fef908e608149d9ebbdffa8fc365f8178649299422e5fa91c5c9e1eaf6@ec2-54-163-240-54.compute-1.amazonaws.com:5432/dfsgi0mppudcls')
    
    #All messages from all group chats are retrieved
    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = 'select * from messages'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #All messages corresponding to a group chat are retrieved 
    def getGroupMessages(self, groupId):    #Maybe add the posibility of IDing groupd by both name and ID.
        cursor = self.conn.cursor()
        query = 'select msgId, content, username, (select count(*) from likes where likes.msgId = messages.msgId) as likes, (select count(*) from dislikes where dislikes.msgId = messages.msgId) as dislikes from messages natural inner join users where groupId = %s'
        cursor.execute(query,(groupId,))
        result = cursor.fetchall()
        return result
        
    #A message that corresponds to the given ID is searched in the corresponding group chat
    def getMessage(self, gName, id):
        for g in self.groupNames:
            if g == gName:
                for m in self.data[self.groupIds[g]]:
                    if id == m['id']:
                        return m
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

