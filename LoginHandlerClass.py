### Author: Gary

#################################################################################################
# DO NOT CHANGE ANYTHING IN THIS FILE!
# IF YOU NEED SOME >CHANGE<, PLEASE CONTACT ME AND LEAVE A COMMENT ABOVE
# ABOUT THE CHANGES YOU NEED. THANKS!!


#################################################################################################
# usage of this class to implement gui:
# need to create a new object of this class by calling it from inside a function that used as 'command' in GUI
# inside the button-command-function call this class in form: <variable> = LoginHandler(<Uid>, <Upw>)
# where <variable> will hold the return value of the object [False or valid UID]
# and <Uid> will be the value of the ID tkinter entry field
# and <Upw> will be the value of the password tkinter entry field
# in the button-command-function should be handled the data [UID] pass-on to the next function, OR
# I propose to create a USER class/object after a valid login in the main file, and set the ID as attribute
# in this way all its info stored in the USER object will be accessible until the program ends
# or optionally, until we kill/delete the object intentionally ( = log out)


from dbHandler import *

class LoginHandler(object):
        #class-wide shared variables
        crDB = DbConn("db/crDB.db")
        c = crDB.cursor
        loggedOn = ""
        loginMessage = ""

        # python constructor method
        def __init__(self, Uid, Upw):
            #object-level variables, unique to every object
            self.userID = Uid
            self.userPassword = Upw
            self.loggedOn = self.login()




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

        def validateInput(self):
            #returnVal = False
            dbPassword = self.fetchUserPw()
            if dbPassword == False:
                self.loginMessage = "Validate: Login failed."
                print(self.loginMessage)
                returnVal = False
            elif dbPassword != False: #may check for "" string with AND here also
                if dbPassword == self.userPassword:
                    self.loginMessage = "Validate: Authentication successful."
                    print(self.loginMessage)
                    returnVal = self.userID
                else:
                    self.loginMessage = "Validate: Password mismatch."
                    returnVal = False
            else:
                self.loginMessage = "Unknown error: No valid password retrieved."
                print(self.loginMessage)
                returnVal = False
            return returnVal

        def login(self):
            return self.validateInput()

#################################################################################################
# usage of this class to implent gui:
# need to create a new object of this class by calling it from inside a function that used as 'command' in GUI
# inside the button-command-function call this class in form: <variable> = LoginHandler(<Uid>, <Upw>)
# where <variable> will hold the return value of the object [False or valid UID]
# and <Uid> will be the value of the ID tkinter entry field
# and <Upw> will be the value of the password tkinter entry field
#

#################################################################################################
#just comment out these lines if you need to work on this file, but leave them as is, thanks
#st147707702
#17159114703
#p@ssword

#manually create a new object called logi with manual inputs
#logi = LoginHandler("st147707702","p@ssword")


# logi = LoginHandler("asdjkfh","p@ssword")   # 'logi' could be anything else of your choice
# print( "True teacher login: " )   # no need to print it, that's for testing purposes
# print( logi.login() )   # no need to print it, that's for testing purposes
# print( logi.loginMessage + "\n" )   # no need to print it, that's for testing purposes
#
# logi = LoginHandler("st147707702","p@ssword")   # 'logi' could be anything else of your choice
# print( "True teacher login: " )   # no need to print it, that's for testing purposes
# print( logi.login() )   # no need to print it, that's for testing purposes
# print( logi.loginMessage + "\n" )   # no need to print it, that's for testing purposes
#
# logi = LoginHandler("st147707702","sdfjldskjf")   # 'logi' could be anything else of your choice
# print( "Flase teacher login: " )   # no need to print it, that's for testing purposes
# print( logi.login() )   # no need to print it, that's for testing purposes
# print( logi.loginMessage + "\n")   # no need to print it, that's for testing purposes
#
# logi = LoginHandler("17159114703","p@ssword")   # 'logi' could be anything else of your choice
# print( "True student login: " )   # no need to print it, that's for testing purposes
# print( logi.login() )   # no need to print it, that's for testing purposes
# print( logi.loginMessage + "\n" )   # no need to print it, that's for testing purposes
#
# logi = LoginHandler("17159114703","LKSADFJLK")   # 'logi' could be anything else of your choice
# print( "Flase student login: " )   # no need to print it, that's for testing purposes
# print( logi.login() )   # no need to print it, that's for testing purposes
# print( logi.loginMessage + "\n" )   # no need to print it, that's for testing purposes


#################################################################################################

