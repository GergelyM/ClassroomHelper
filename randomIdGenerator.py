# description of algorithm:
# the ID consist 7 characters, char. 1-2 is either the short form of the actual year (student), or two letters (teacher)
# the following 5 characters the last 5 digits of the actual time stamp in secs.
# generating 100.000/10.000/1.000/500/100 numbers from time stamp shows near 0 redundancy, although
# to ensure the product is unique, the function will do a lookup in the database for existence
# it will continue generating new ids until finally find a unique one

import time
import dbHandler

#build DB connection
crDB = dbHandler.DbConn("db/crDB.db")
c = crDB.cursor

#stores the existing id numbers
allStudentIds = []  #stores the existing id numbers
allTeacherIds = []


#################################################
# this function supports the others

def fetchAllUserID():
    # fetch the ID of students and of teachers and store them in lists
    newSq = "SELECT studentID FROM student"
    c.execute(newSq)
    list = c.fetchall()
    for i in list:
        allStudentIds.append(i[0][-5:])
    newSq = "SELECT teacherID FROM teacher"
    c.execute(newSq)
    list = c.fetchall()
    for i in list:
        allTeacherIds.append(i[0][-5:])

#################################################
# call this function to get a new studentID

def oneNewStudentId():
    fetchAllUserID()
    studentId = ""
    currentYear = time.strftime("%y")  # this gives back the current year in 2-digit format
    for i in range(0, 500):
        milsec = str(time.time())
        milsec = milsec[-5:]
        if milsec not in allStudentIds:
            studentId = str(currentYear + milsec)
            break
    return studentId

#################################################
# call this function to get a new teacherID

def oneNewTeacherId():
    fetchAllUserID()
    teacherId = ""
    for i in range(0, 500):
        milsec = str(time.time())
        milsec = milsec[-5:]
        if milsec not in allTeacherIds:
            teacherId = str("st" + milsec)
            break
    return teacherId


#print(allStudentIds)
#print(allTeacherIds)
#print("one new studentID: " + oneNewStudentId() )
#print("one new teacherID: " + oneNewTeacherId() )

#################################################
## TEST OF THE GENERATOR ALGORITHM, uncomment the lines below
#
# setOfnums = []      #newly generated numbers for testing
# fetchAllUserID()
# for i in range(0, 100):  #changing the range to higher number allow us to test the reliability of the generator
#     milsec = str(time.time())
#     milsec = milsec[-5:]
#     if milsec not in allStudentIds:
#         setOfnums.append(milsec)
#         #print(milsec)
#
# print( len(setOfnums) )     # the code do a match check in existing ID's, the number of skipped iterations indicate
#                             # the error margin, at such a small number of students
# print( setOfnums )
#
#################################################

#sample db connection
# newSq = ("SELECT teacherPassword FROM teacher WHERE teacherID = ?", variable)
# c.execute(newSq)