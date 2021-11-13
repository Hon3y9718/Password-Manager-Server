import firebase_admin
from firebase_admin import credentials, firestore

class FirestoreDB():
    def __init__(self):
        cred = credentials.Certificate('app\passwordmanager-b5607-firebase-adminsdk-xe29w-7231e1607a.json')
        default_App = firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def getCopiedPassword(self, uid):
        try:
            user_Ref = self.db.collection(u"user").where(u"uid" , u"==", u"{}".format(uid)).get()
            user = user_Ref[0].to_dict()
            userEmail = user['Email']
            self.doc_ref = self.db.collection(u"user").document(u"{}".format(userEmail)).collection(u"copiedPassword")
            passwordRef_Data = self.doc_ref.get()
            PasswordRef_Data_toDict = passwordRef_Data[0].to_dict()
            Password_Ref = PasswordRef_Data_toDict['ref']
            passwordDoc = self.db.collection(u"user").document(u"{}".format(userEmail)).collection(u"passwords").where(u"ID", u"==", u"{}".format(Password_Ref))
            doc = passwordDoc.get()
            return doc[0].to_dict()
        except Exception as e:
            if (e is not None):
                print(e)
            return None
       