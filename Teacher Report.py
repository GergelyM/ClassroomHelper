from dbHandler import *

class teacherReport(object):
    #Establishes connection with the database
    crDB = DbConn("db/crDBv2.db")
    c = crDB.cursor

    #Constructor
    def __init__(self, teacherID, year):
        self.teacherID = teacherID
        self.year = year
        self.year = str(self.year)

    #Gets group ID that selected teacher teaches at  a given year.
    def getGroupID (self):
        groupID = "SELECT groupsetID, moduleCode FROM groupset WHERE teacherID = '" + self.teacherID + "'" + "AND year = '" + self.year + "'"
        self.c.execute(groupID)
        self.receivedID = self.c.fetchone()
        return self.receivedID[0], self.receivedID[1]

    #Gets IDs of every student within the group
    def getStudentID(self):
        id = self.receivedID[0]
        id = str(id)
        studentID = "SELECT studentID FROM grade WHERE groupsetID = '" + id + "'"
        self.c.execute(studentID)
        self.stuID = self.c.fetchall()
        return self.stuID

    #Gets grades for every studen t
    def getGrades(self):
        id = self.receivedID[0]
        id = str(id)
        studentGrade = "SELECT gradeType FROM grade WHERE groupsetID = '" + id + "'"
        self.c.execute(studentGrade)
        self.stuGrade = self.c.fetchall()
        return self.stuGrade

    #Puts received data together in a list
    def createReport(self):
        self.getGroupID()
        teacherReport = ("Groupset ID: ", self.receivedID[0], "Module Number: ", self.receivedID[1], "Student's ID: ", self.getStudentID(),"Student's Grade: ", self.getGrades())
        return teacherReport

# For testing:
# a = teacherReport("st84508", 2017)
# a.getGroupID()
# a.getStudentID()
# a.getGrades()
# a.createReport()
