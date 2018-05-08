from flask import jsonify
import psycopg2
from config import db_config

class ReactionsDAO():
    def __init__(self):
        #maybe jsut add el url del DB directly?
        connection_url = "dbname=%s user=%s password=%s" % (db_config['dbname'],  db_config['user'], db_config['passwd'])
        self.conn = psycopg2._connect('postgres://rdoycbxokxgmsz:d9980f20415499517e3caacaa67ee00376d331677988af4b8c4887fc65235efc@ec2-75-101-142-91.compute-1.amazonaws.com:5432/d2o9j3bddfg00r')

    def getMsgLikesCount(self, msgId):
        cursor = self.conn.cursor()
        query = 'select count(*) from likes where msgId= %s'
        cursor.execute(query,(msgId,))
        result = cursor.fetchone()
        return result

    def getMsgDislikesCount(self, msgId):
        cursor = self.conn.cursor()
        query = 'select count(*) from dislikes where msgId= %s'
        cursor.execute(query,(msgId,))
        result = cursor.fetchone()
        return result

    def getLikeList(self,msgId):
        cursor = self.conn.cursor()
        query = 'select m2.username from likes as l inner join users as m2 on l.userid= m2.userid where l.msgId = %s;'
        cursor.execute(query,(msgId,))
        result=[]
        for row in cursor:
            result.append(row)
        return result
    
    def getDislikeList(self,msgId):
        cursor = self.conn.cursor()
        query = 'select m2.username from dislikes as dl inner join users as m2 on dl.userid= m2.userid where dl.msgId = %s;'
        cursor.execute(query,(msgId,))
        result=[]
        for row in cursor:
            result.append(row)
        return result