### Author: Salik, Gary
from dbHandler import *
from tkinter import *

class LoginHandler(object):
        root = Tk()
        crDB = DbConn("db/crDB.db")
        c = crDB.cursor

        def __init__(self):
            self.userID = None
            self.userPassword = None

        def readInput(self):
            self.userID = self.EntryID.get()
            self.userPassword = self.EntryPassword.get()

        labelID = Label(root, text="ID").grid(row=0, sticky=E)
        labelPassword = Label(root, text="Password").grid(row=1, sticky=E)
        EntryID = Entry(root).grid(row=0, column=1)
        EntryPassword = Entry(root, show="*").grid(row=1, column=1)

        def fetchUserPw(self):
            newSq = ""
            try:
                if self.userID[0:1].isnumeric():
                    newSq = "SELECT studentPassword FROM student WHERE studentID = '" + self.userID + "'"
                if self.userID[0:2] == "st":
                    newSq = "SELECT teacherPassword FROM teacher WHERE teacherID = '" + self.userID + "'"
                self.c.execute(newSq)
                self.fetchedPw = self.c.fetchone()[0]
            except TypeError:
                self.fetchedPw = False
            return self.fetchedPw

        button = Button(root, text="Submit", command=fetchUserPw).grid(row=2, column=2)

        def repeatInput(self):
            loopControl = True
            counter = 3
            returnVal = False

            while counter > 0 and loopControl != False:
                self.readInput()

                dbPassword = self.fetchUserPw()
                if dbPassword == False:
                    if counter > 0:
                        print("Please try again.")
                    else:
                        print("Login failed.")
                    counter -= 1
                elif dbPassword != False: #may check for "" string with AND here also
                    if dbPassword == self.userPassword:
                        print("Authentication successful, please proceed.")
                        returnVal = self.userID
                        loopControl = False
                    else:
                        counter -= 1
                else:
                    counter -= 1
            return returnVal

        root.mainloop()

        def login(self):
            return self.repeatInput()


logi = LoginHandler()   # 'logi' could be anything else of your choice
print( logi.login() )   # no need to print it, that's for testing purposes
