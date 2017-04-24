###########################################################################
#
# Class used to hold the information of the actual logged on user details.
# Will be deleted on program close.
#
###########################################################################

from dbHandler import *

class activeUserClass(object):
        # class-wide shared variables
        _crDB = DbConn("db/crDB.db")
        _c = _crDB.cursor
        # actual object variables _ means protected
        _userType = ""
        _userID = ""
        _userName = ""
        _userSurname = ""
        _userEmail = ""

        def setUpObject(self, uid):
            self.setUID(uid)
            if self._userID[0:2].isnumeric():
                self._userType = "student"
            if self._userID[0:2] == "st":
                self._userType = "teacher"
            self.getUserData()
            #print("userObject has been setup")
            #print(self.getType())

        def getUID(self):
            return self._userID

        def setUID(self, uid):
            self._userID = uid
            if self._userID[0:2].isnumeric():
                self._userType = "student"
            if self._userID[0:2] == "st":
                self._userType = "teacher"
            self.getUserData()

        def getType(self):
            return self._userType

        def getName(self):
            return self._userName

        def getSurname(self):
            return self._userSurname

        def getFullname(self):
            fullname = self._userName + " " + self._userSurname
            return fullname

        def getUserData(self):
            if self._userType == "student":
                self._c.execute("SELECT studentSurname, studentName FROM student WHERE studentID ='" + self._userID + "'")
            if self._userType == "teacher":
                self._c.execute("SELECT teacherSurname, teacherName FROM teacher WHERE teacherID ='" + self._userID + "'")
            fetchedData = self._c.fetchone()
            self._userName = fetchedData[0]
            self._userSurname = fetchedData[1]
