from dao.user_dao import UserDAO
dao = UserDAO()
class ContactlistDAO():

    def __init__(self):
        
        contList1= Contactlist(001, 7001,[4405,8569,5567])
        contList2= Contactlist(002, 4405,[5567])
        contList3= Contactlist(121, 8569,[7001,5567])
        contList4= Contactlist(561, 5567,[8569,7001])

        self.data = []
        self.data.append(contList1.mapContactlistToDict())
        self.data.append(contList2.mapContactlistToDict())
        self.data.append(contList3.mapContactlistToDict())
        self.data.append(contList4.mapContactlistToDict())
    
    def getAllContacts(self, IdUser):
         #returns list of the ID's oc the contacts
        result = []
        for r in self.data:
            if IdUser == r['IdOwner']:
                result=r['IdContacts']
        mappedContacts = []
        for r in result:
            mappedContacts.append({
                'IdUser':dao.getUserById(r)['IdUser'],
                'uFirstName':dao.getUserById(r)['uFirstName'],
                'phone':dao.getUserById(r)['phone']})
        toco= {}
        toco = {"User's "+str(IdUser)+" contacts": mappedContacts}
        return toco

         

    def getContactlistOwner():
        return self.data[1]
    



class Contactlist():
    def __init__(self, IdContactlist, IdOwner, IdContacts):
        self.IdContactlist = IdContactlist
        self.IdOwner = IdOwner
        self.IdContacts = IdContacts
    
    #Getters

    def getIdContactlist(self):
        return self.IdContactlist
    
    def getIdOwner(self):
        return self.IdOwner
    
    def getIdContacts(self):
        return self.IdContacts
    
    #Turn attribute into a dictionary
    def mapContactlistToDict(self):
        mappedContactlist = {}
        mappedContactlist['IdContactlist'] = self.getIdContactlist()
        mappedContactlist['IdOwner'] = self.getIdOwner()
        mappedContactlist['IdContacts'] = self.getIdContacts()
        return mappedContactlist