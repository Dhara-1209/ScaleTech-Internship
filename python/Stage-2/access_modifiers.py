class User:
    def __init__(self,username,email,password):
        self.username=username #public
        self._email=email   #proctected
        self.__password=password    #private

    def showDetails(self):
        print("Username:",self.username)
        print("Email:",self._email)
        print("Password:*****")

    def change_password(self,old_password,new_password):
        if self.__password==old_password:
            self.__password= new_password
            print("Password changed successfully")
        else:
            print("Incorrect old password")

u1=User("Dhara","dhara6744@gmail.com","12345abc")
u1.showDetails()
# print(u1.__password)

u1.change_password("12345abc", "newpass456")
u1.showDetails()
        