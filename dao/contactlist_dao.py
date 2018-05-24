from dao.user_dao import UserDAO
from config import db_config
import psycopg2


#Function to map the results of the query into a dictionary.
def mapToDict(row):
    mappecContactList = {}
    mappecContactList['ownerId'] = row[0]
    mappecContactList['userId'] = row[1]
    return mappecContactList

class ContactlistDAO():

    def __init__(self):
        #Getting some probles mis this so added el url del DB directly, for the time being.
        connection_url = "dbname=%s user=%s password=%s" % (db_config['dbname'],  db_config['user'], db_config['passwd'])
        self.conn = psycopg2._connect('postgres://rdoycbxokxgmsz:d9980f20415499517e3caacaa67ee00376d331677988af4b8c4887fc65235efc@ec2-75-101-142-91.compute-1.amazonaws.com:5432/d2o9j3bddfg00r')
    
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
    