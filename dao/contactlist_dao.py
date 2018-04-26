from dao.user_dao import UserDAO
from config import db_config
import psycopg2

dao = UserDAO()

def mapToDict(row):
    mappecContactList = {}
    mappecContactList['ownerId'] = row[0]
    mappecContactList['userId'] = row[1]
    return mappecContactList

class ContactlistDAO():

    def __init__(self):
        #maybe jsut add el url del DB directly?
        connection_url = "dbname=%s user=%s password=%s" % (db_config['dbname'],  db_config['user'], db_config['passwd'])
        self.conn = psycopg2._connect('postgres://ekabibbfjhmljk:ea67f5fef908e608149d9ebbdffa8fc365f8178649299422e5fa91c5c9e1eaf6@ec2-54-163-240-54.compute-1.amazonaws.com:5432/dfsgi0mppudcls')
    
    def getAllContacts(self, ownerId):
        cursor = self.conn.cursor()
        query = 'select userid,firstname,lastname,username,phonenumber,email from users inner join contactlist c2 on users.userid = c2.contactid where ownerid = %s;'
        cursor.execute(query,(ownerId,))
        result = []
        for ror in cursor:
            result.append(ror)
        return result

         

    def getContactlistOwner():
        return self.data[1]
    