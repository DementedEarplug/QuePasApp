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
    
    def addToContact(self, userID, info):
        cursor = self.conn.cursor()
        t1 = "with t1 as (select userid from users where userid = %s),"
        t2 =  "t2 as (select userid from users where phonenumber = %s or email = %s),"
        t3 = "t3 as (select count(*) as count from contactlist inner join users on contactid = userid where ownerid = %s and (email = %s or phonenumber = %s)) "
        t4 = "select t1.userid as owner, t2.userid as contact, t3.count from t1,t2,t3"
        query = t1+t2+t3+t4
        print(info)
        cursor.execute(query, [userID, info['phone'], info['email'], userID, info['email'], info['phone']])
        result = cursor.fetchone()
        print(result)
        if(len(result)>0 and result[2]==0):
            query = 'insert into contactlist (ownerid, contactid) values(%s, %s)'
            cursor.execute(query, [userID, result[1]])
            self.conn.commit()
            return 'Contact Added'
        else:
            return "Can't add contact"
            

         

    #def getContactlistOwner():
    #    return self.data[1]
    