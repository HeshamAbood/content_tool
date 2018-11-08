
class User():

    def __init__(self, *args, **kwargs):
        pass

    def userLogin(self):
        self.login=True

    def verifyLogin(self):
        return self.login==True

    def userLogout(self):
        self.login==False

    def modifyPassowrd(self, newPassowrd):
        pass
        #connect to db and modfiy the new passowrd
