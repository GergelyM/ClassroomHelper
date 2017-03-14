###########################################################################
#
# Class used to hold the information of the actual logged on user details.
# Will be deleted on program close.
#
###########################################################################

from dbHandler import *

class activeUserClass(object):
        #class-wide shared variables
        crDB = DbConn("db/crDB.db")
        c = crDB.cursor

        # records from 'student' table
        # id, studentID, studentGender, studentSurname, studentName, studentEmail, studentPassword
        # records from 'teacher' table
        # id, teacherID, teacherTitle, teacherSurname, teacherName, teacherEmail, teacherPassword

        userType = ""
        userID = ""
        userName = ""
        userSurname = ""
        userEmail = ""

        # def __init__(self, uid):
        #     self.userID = uid
        #     if self.userID[0:2].isnumeric():
        #         self.userType = "student"
        #     if self.userID[0:2] == "st":
        #         self.userType = "teacher"

        def setUID(self, uid):
            self.userID = uid
            if self.userID[0:2].isnumeric():
                self.userType = "student"
            if self.userID[0:2] == "st":
                self.userType = "teacher"
            self.getUserData()

        def getUserData(self):
            if self.userType == "student":
                self.c.execute("SELECT studentSurname, studentName FROM student WHERE studentID ='" + self.userID + "'")
            if self.userType == "teacher":
                self.c.execute("SELECT teacherSurname, teacherName FROM teacher WHERE teacherID ='" + self.userID + "'")
            fetchedData = self.c.fetchone()
            self.userName = fetchedData[0]
            self.userSurname = fetchedData[1]
