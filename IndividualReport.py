from dbHandler import *

class individualReport(object):
    #Establishes connection with the database
    crDB = DbConn("db/crDBv2.db")
    c = crDB.cursor

    #Constructor
    def __init__(self, studentID, year):
        self.studentID = studentID
        self.year = year
        self.year = str(self.year)

    #Gets grades and modules that selected student takes in a given year.
    def getGrade (self):
        grade = "SELECT gradeType, moduleCode FROM groupset INNER JOIN grade ON groupset.groupsetID = grade.groupsetID WHERE studentID = '" + self.studentID + "'"
        self.c.execute(grade)
        self.receivedGrade = self.c.fetchone()
        return self.receivedGrade[0], self.receivedGrade[1]

    # Returns total number of lectures student attended in a given year.
    def getAttendance(self):
        attendance = "SELECT attendTotal FROM attendance WHERE studentID = '" + self.studentID + "'"
        self.c.execute(attendance)
        self.recAttendance = self.c.fetchone()
        return self.recAttendance

    # Puts received data together in a list
    def createReport(self):
        self.getGrade()
        self.getAttendance()
        report = ("Student ID: ", self.studentID, " / " ,"Year: ", self.year, " / ", "Module: ", self.receivedGrade[1], " / ", "Grade: ", self.receivedGrade[0], " / ", "Attendance: ", self.recAttendance)
        return report

# For testing:
# a = individualReport("1733675", 2017)
# a.getGrade()
# a.getAttendance()
# a.createReport()
