from dbHandler import *
from tkinter import *

class LoginHandler:
        crDB = DbConn("db/crDB.db")
        c = crDB.cursor

        def __init__(self, master):

            self.master = master
            #Creates ID and password label s
            self.labelID = Label(master, text="ID").grid(row=0, sticky=E)
            self.labelPassword = Label(master, text="Password").grid(row=1, sticky=E)

            #Creates input entries
            self.EntryID = Entry(master)
            self.EntryID.grid(row=0, column=1)
            self.EntryPassword = Entry(master, show="*")
            self.EntryPassword.grid(row = 1, column = 1)

            #Creates a sign in button
            self.button = Button(master, text = "Sign in", command = self.login)
            self.button.grid(row = 2, column = 2)

            #for testing purposes
            #17159114703
            #p@ssword

        def readInput(self):
            self.userID = self.EntryID.get()
            self.userPassword = self.EntryPassword.get()

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

        def repeatInput(self):
            loopControl = True
            counter = 3
            returnVal = False

            while counter > 0 and loopControl != False:
                self.readInput()

                dbPassword = self.fetchUserPw()
                if dbPassword == False:
                    if counter > 0:
                        self.successfulLogin = Label(self.master, text="Please try again.").grid(row=2, column=1)
                    else:
                        self.successfulLogin = Label(self.master, text="Login failed.").grid(row=2, column=1)

                    counter -= 1
                elif dbPassword != False:
                    if dbPassword == self.userPassword:
                        self.successfulLogin = Label(self.master, text="Authentication successful").grid(row=2, column = 1)
                        returnVal = self.userID
                        loopControl = False
                    else:
                        counter -= 1
                else:
                    counter -= 1
            return returnVal

        def login(self):
            return self.repeatInput()

root = Tk()
gui = LoginHandler(root)
root.mainloop()
