### Author: Salik, Gary
### Trasferred from Pulled project file by Gary

# it would be a bit more efficient if you would use a single data query for the user by login input name
# in that way the code could decide if the input name exists in the DB,
# and if it does, then that the stored password is equal to the user input
# I will write the SQL statement here so you can just fit it in your code.
# well practically I'll make a variable with the db field values above.

from dbHandler import *

#################################################################################################
# DO NOT CHANGE ANYTHING HERE, PLEASE!
# IF YOU NEED SOME >CHANGE<, PLEASE LEAVE A COMMENT ABOVE. THANKS!!

class LoginHandler(object):
        #class-wide shared variables
        crDB = DbConn("db/crDB.db")
        c = crDB.cursor

        def __init__(self):
         #python constructor method
            #object-level variables, unique to every object
            self.userID = None
            self.userPassword = None

        def readInput(self):
            self.userID = input("Enter ID: ")
            self.userPassword = input("Enter password: ")

        def fetchUserPw(self):
            #this reads the object variables from __init__ method, to fetch data from DB
            newSq = ""
            try:
                if self.userID[0:1].isnumeric():
                    newSq = "SELECT studentPassword FROM student WHERE studentID = '" + self.userID + "'"
                if self.userID[0:2] == "st":
                    newSq = "SELECT teacherPassword FROM teacher WHERE teacherID = '" + self.userID + "'"
                self.c.execute(newSq)
                fetchedPw = self.c.fetchone()[0]
            except TypeError:
                fetchedPw = False
            #this returns the stored password belongs to the userID
            return fetchedPw

        def repeatInput(self):
            #repeatedly asks for user input, until match, or number of tries used up, whichever happens first
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
            #tested for 3x wrong ID & wrong pass; 3x good teacher ID & wrong pass; 3x good studentId & wrong pass, returns False
            #tested for 2x fail attempt + 1x good student Id & good pass, returns the ID
            #tested for 2x fail attempt + 1x good teacher Id & good pass, returns the ID

        def login(self):
            return self.repeatInput()

#################################################################################################
#just comment out these lines if you need to work on this file, but leave them as is, thanks
#st147707702
#17159114703
#p@ssword
logi = LoginHandler()
print( logi.login() )

#################################################################################################

