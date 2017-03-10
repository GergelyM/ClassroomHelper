### Author: Salik, Gary
### Trasferred from Pulled project file by Gary

# it would be a bit more efficient if you would use a single data query for the user by login input name
# in that way the code could decide if the input name exists in the DB,
# and if it does, then that the stored password is equal to the user input
# I will write the SQL statement here so you can just fit it in your code.
# well practically I'll make a variable with the db field values above.

from dbHandler import *
from tkinter import *

#################################################################################################
# DO NOT CHANGE ANYTHING HERE, PLEASE!
# IF YOU NEED SOME >CHANGE<, PLEASE LEAVE A COMMENT ABOVE. THANKS!!

class LoginHandler:
        # class-wide shared variables
        crDB = DbConn("db/crDB.db")
        c = crDB.cursor

        def __init__(self, master):
            # python constructor method
            # object-level variables, unique to every object
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
            # this reads the object variables from __init__ method, to fetch data from DB
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
            # this returns the stored password belongs to the userID
            return self.fetchedPw

        def repeatInput(self):
            # repeatedly asks for user input, until match, or number of tries used up, whichever happens first
            loopControl = True
            # adding a counter here could be use to count/restrict failed attempts
            counter = 3
            returnVal = False

            while counter > 0 and loopControl != False:
                self.readInput()
                # self.fetchUserPw() can have 3 value: None (default), False (userId wrong)
                # or the actual password if the UserID is valid (but the password is not, fails login though)
                dbPassword = self.fetchUserPw()
                if dbPassword == False:
                    if counter > 0:
                        self.successfulLogin = Label(self.master, text="Please try again.").grid(row=2, column=1)
                    else:
                        self.successfulLogin = Label(self.master, text="Login failed.").grid(row=2, column=1)
                    counter -= 1
                elif dbPassword != False: #may check for "" string with AND here also
                    if dbPassword == self.userPassword:
                        self.successfulLogin = Label(self.master, text="Authentication successful").grid(row=2, column = 1)
                        returnVal = self.userID
                        loopControl = False
                    else:
                        counter -= 1
                else:
                    counter -= 1
            return returnVal
            # tested for 3x wrong ID & wrong pass; 3x good teacher ID & wrong pass; 3x good studentId & wrong pass, returns False
            # tested for 2x fail attempt + 1x good student Id & good pass, returns the ID
            # tested for 2x fail attempt + 1x good teacher Id & good pass, returns the ID

        def login(self):
            return self.repeatInput()

#################################################################################################
#just comment out these lines if you need to work on this file, but leave them as is, thanks
#st147707702
#17159114703
#p@ssword

#root = Tk()
#gui = LoginHandler(root)
#root.mainloop()

#################################################################################################