#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#FCK tinyDB, ditched for good, too complicated to be called "small and easy"

import sqlite3
from datetime import *
import os
from random import randint

#TODO-Gary sort out imports, more organised, move os to the only function uses it
#TODO-Gary Generate final data to each table

#TODO-Gary create a dbConn Class to handle the connection
#TODO-Gary test DbConn() Class
class DbConn(object):
    def __init__(self, dbPath):  #object/class constructor, everything in __init__ will be called when a copy of the class being created
        self.connection = sqlite3.connect(dbPath)
        self.connection.execute('pragma foreign_keys = on')
        self.connection.commit()
        self.cursor = self.connection.cursor()

    def query(self, arg):
        self.cursor.execute(arg)
        data = self.cursor.fetchall()   # fetchall() make it possible to use 'list[n][k]' call on the fetched data directly
        self.connection.commit()
        #return self.cursor
        return data

    def __del__(self):
        self.connection.close()

    # check and create db
    # renamed to fit better to SqLite
    def initDB(dbConn):
        if not os.path.isdir("./db"):  # if this won't work well use os.path.exists(<path>)
            os.makedirs("./db")  # at this level of the project it sould just rely on an existing DB on path
            createDB = sqlite3.connect('db/crDB.db')
            createTables()
            populateControl()
        elif not os.path.isfile("./db/crDB.db"):
            createDB = sqlite3.connect('db/crDB.db')
            createTables()
            populateControl()
        else:
            createDB = sqlite3.connect('db/crDB.db')
            populateControl()
        return createDB

        # def checkNcreateDB():
        #     # reworked to make the initilaisation more readable
        #     crDB = initDB()
        #     return crDB


        # start up DB
        # crDB = initDB()



#TODO-Gary write a generic, unique userID generator // DONE for students
#use given data find in DB: initials, date of birth, and current date
#rename function for more generic name : from genStdNum() to genIdNum()
def genIdNum(name, surname, dateOfBirth, role):
    currentYear = date.today().strftime("%y") #this gives back the current year in 2-digit format
    fInitial = ord(name[0])
    sInitial = ord(surname[0])
    dof = dateOfBirth.split("/")    #the correct date format: dd/mm/yyyy
    dof[2]=dof[2][-2::]
    if role == "student" :
        uniqueID = "%s%s%s%s%s%s" % (currentYear, fInitial + sInitial, randint(0,9), dof[0], randint(0,9), dof[1])
    elif role == "teacher":
        uniqueID = "%s%s%s%s%s%s" % ("st", fInitial + sInitial, randint(0,9), dof[0], randint(0,9), dof[1])
    else:
        uniqueID = "%s%s%s%s%s%s" % (currentYear, fInitial + sInitial, randint(0,9), dof[0], randint(0,9), dof[1])
    return uniqueID

#TODO-Gary add comments to this function
#renamed to fit a more generic role from generateRandomStudent() to generateRandomPerson(role)
def generateRandomPerson(role):
    nameFile = open("teststuff/names.txt","r")
    fullNameList = nameFile.readlines()
    nameFile.close()
    name = []
    surname = []
    for line in fullNameList:
        line = line.rstrip("\n")
        nameSplit = line.split(" ")
        name.append(nameSplit[0])
        surname.append(nameSplit[1])
    randOne = randint(0, len(name)-1)
    randTwo = randint(0, len(surname)-1)
    dateFile = open("teststuff/dates.txt","r")
    allDates = dateFile.readlines()
    dateFile.close()
    i = 0
    while (i < len(allDates)):
        allDates[i] = allDates[i].rstrip("\n")
        i+=1
    randThree = randint(0,len(allDates)-1)
    genID = genIdNum(name[randOne], surname[randTwo], allDates[randThree], role)
    # id, studentID TEXT, studentTitle TEXT, studentName TEXT, studentSurname TEXT, studentDateOfBirth TEXT, studentPassword TEXT
    if role == "student" :
        randomStudent = ( genID,"",name[randOne],surname[randTwo],allDates[randThree],"p@ssword" )
    elif role == "teacher":
        randomStudent = (genID, "", name[randOne], surname[randTwo], "p@ssword")
    return randomStudent

#TODO-Gary check if studentID exist in DB
#TODO-Gary check and add real password later
#renamed to reflect is function better from: insertXRndStudent(x) to populateStudentTable(x)
def populateStudentTable(x):
    crDB = sqlite3.connect('db/crDB.db')
    studentBatch = []
    i=0
    while (i <= x):
        studentBatch.append(generateRandomPerson("student"))
        i += 1
    cursor2 = crDB.cursor()
    cursor2.executemany('INSERT INTO student(studentID, studentTitle, studentName, studentSurname, studentDateOfBirth, studentPassword) VALUES (?,?,?,?,?,?)', studentBatch)
    crDB.commit()
    #maybe it should return with a True on success
    #exception handling would be a good solution (try/except)


def populateModuleTable():
    crDB = sqlite3.connect('db/crDB.db')
    #TODO-Gary create an algorithm generates module uniqueID, eid could be used for that
    #TODO-Gary describe modulecode //DONE
    # id, moduleCode TEXT, moduleName TEXT, moduleDescription TEXT
    tableModule = []
    tableModule.append( ("M01001","Art of nothing","Nobody helped me out, so no description, you write better if you want") )
    tableModule.append( ("M01003","How to tip a cow","Nobody helped me out, so no description, you write better if you want") )
    tableModule.append( ("M02001","Chololate unwrapping Studies","Nobody helped me out, so no description, you write better if you want") )
    tableModule.append( ("M03001","How to oreder at McD. efficiently","Nobody helped me out, so no description, you write better if you want") )
    tableModule.append( ("M03010","Spliff Rollin\' Course","Nobody helped me out, so no description, you write better if you want") )
    tableModule.append( ("M03011","Do WHATEVER professionally","Nobody helped me out, so no description, you write better if you want") )
    cursor3 = crDB.cursor()
    cursor3.executemany('''INSERT INTO module(moduleCode, moduleName, moduleDescription) VALUES (?,?,?)''', tableModule)
    crDB.commit()
    # # maybe it should return with a True on success
    # exception handling would be a good solution (try/except)

def populateTeacherTable(x):
    crDB = sqlite3.connect('db/crDB.db')
    teacherBatch = []
    i = 0
    while (i <= x):
        teacherBatch.append(generateRandomPerson("teacher"))
        i += 1
    #id, teacherID, teacherTitle, teacherName, teacherSurname, teacherPassword
    cursor2 = crDB.cursor()
    cursor2.executemany(
        'INSERT INTO teacher(teacherID, teacherTitle, teacherName, teacherSurname, teacherPassword) VALUES (?,?,?,?,?)',
        teacherBatch)
    crDB.commit()
    # maybe it should return with a True on success
    # exception handling would be a good solution (try/except)

#now the tricky stuff
#add some teachedby rows
#year, semester, teacherID, moduleCode, FOREIGN KEY(teacherID), FOREIGN KEY(moduleCode), PRIMARY KEY (teacherID, moduleCode)
def populateTeachedbyTable(x):
    crDB = sqlite3.connect('db/crDB.db')
    c4 = crDB.cursor()
    i = 0
    for i in range(0,x):
        c4.execute('SELECT teacherID FROM teacher ORDER BY random() LIMIT 1')
        randomTeacherID = c4.fetchone()[0]
        c4.execute('SELECT moduleCode FROM module ORDER BY random() LIMIT 1')
        randomModuleCode = c4.fetchone()[0]
        insertData = (date.today().strftime("%Y"), 1, randomTeacherID, randomModuleCode )
        c4.execute('INSERT INTO teachedby(year, semester, teacherID, moduleCode) VALUES (?,?,?,?)', insertData)
    crDB.commit()

def populateGradeTable(x):
    #grade, year, semester, studentID, moduleCode
    crDB = sqlite3.connect('db/crDB.db')
    c5 = crDB.cursor()
    i = 0
    fallouts = []
    for i in range(0,x):
        c5.execute('SELECT studentID FROM student ORDER BY random() LIMIT 1')
        randomStudentID = c5.fetchone()[0]
        c5.execute('SELECT moduleCode FROM module ORDER BY random() LIMIT 1')
        randomModuleCode = c5.fetchone()[0]
        year = date.today().strftime("%Y")
        grade = randint(38,91)
        semester = randint(1,2)
        insertData = (grade, year, semester, randomStudentID, randomModuleCode)
        if randomStudentID not in fallouts:
            c5.execute('INSERT INTO grade(grade, year, semester, studentID, moduleCode) VALUES (?,?,?,?,?)', insertData)
            fallouts.append(randomStudentID)
    crDB.commit()

#get some sample data out of the DB
def testQueries(crDB):
    #do some test queries from
    c = crDB.cursor
    #c.execute('SELECT * FROM module ORDER BY random() LIMIT 5')
    c.execute('SELECT * FROM module')
    allRows = c.fetchall()
    print("All records from 'module' table")
    for row in allRows:
        print(row)
    #c.execute('SELECT * FROM student ORDER BY random() LIMIT 5')
    c.execute('SELECT * FROM student')
    allRows = c.fetchall()
    print("All records from 'student' table")
    for row in allRows:
        print(row)
    #c.execute('SELECT * FROM teacher ORDER BY random() LIMIT 5')
    c.execute('SELECT * FROM teacher')
    allRows = c.fetchall()
    print("All records from 'teacher' table")
    for row in allRows:
        print(row)
    #c.execute('SELECT * FROM teachedby ORDER BY random() LIMIT 5')
    c.execute('SELECT * FROM teachedby')
    allRows = c.fetchall()
    print("All records from 'teachedby' table")
    for row in allRows:
        print(row)
    #c.execute('SELECT * FROM grade ORDER BY random() LIMIT 5')
    c.execute('SELECT * FROM grade')
    allRows = c.fetchall()
    print("All records from 'grade' table")
    for row in allRows:
        print(row)
    # sample ooutput as is
    print("\nSample raw output:")
    print(allRows)
    print("\n")

# the actual query for authentication
def retrievePW(userID):
    uID = []
    uID.append(userID)
    crDB = sqlite3.connect('db/crDB.db')
    cd = crDB.cursor()
    if (userID[0:2:] == "st"):
        cd.execute('SELECT teacherPassword FROM teacher WHERE teacherID = ?', uID)
        rows = cd.fetchone[0]
        # if len(rows) != 0 :
        #     return rows
    else:
        cd.execute('SELECT studentPassword FROM student WHERE studentID = ?', uID)
        rows = cd.fetchone()[0]
        # if len(rows) != 0 :
        #     return rows
    return rows

#not used at this stage, and probably won't be, as this file supped to be a module only
#if __name__ == "__main__":

#TODO-Gary write an init function to
#check existence of folder -> create folder
#check existence of file -> create file
#check existence of tables one by one -> create tables
#check table(s) for records -> populate table(s)

def createTables():
    crDB = sqlite3.connect('db/crDB.db')
    cursor = crDB.cursor()
    # simplified version no contact details saved now
    # cursor.execute('''CREATE TABLE student( id INTEGER PRIMARY KEY AUTOINCREMENT, studentID TEXT UNIQUE, studentTitle TEXT, studentName TEXT, studentSurname TEXT, studentDateOfBirth TEXT, studentPhone TEXT, studentEmail TEXT UNIQUE, studentPassword TEXT) ''')
    # cursor.execute('''CREATE TABLE teacher( id INTEGER PRIMARY KEY AUTOINCREMENT, teacherID TEXT UNIQUE, teacherTitle TEXT, teacherName TEXT, teacherSurname TEXT, teacherPhone TEXT, teacherEmail TEXT UNIQUE, teacherPassword TEXT) ''')
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS student( id INTEGER PRIMARY KEY AUTOINCREMENT, studentID TEXT UNIQUE, studentTitle TEXT, studentName TEXT, studentSurname TEXT, studentDateOfBirth TEXT, studentPassword TEXT) ''')
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS teacher( id INTEGER PRIMARY KEY AUTOINCREMENT, teacherID TEXT UNIQUE, teacherTitle TEXT, teacherName TEXT, teacherSurname TEXT, teacherPassword TEXT) ''')
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS module( id INTEGER PRIMARY KEY AUTOINCREMENT, moduleCode TEXT UNIQUE, moduleName TEXT, moduleDescription TEXT ) ''')
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS grade(grade INTEGER, year INTEGER, semester INTEGER, studentID TEXT, moduleCode TEXT, FOREIGN KEY(studentID) REFERENCES student(studentID), FOREIGN KEY(moduleCode) REFERENCES module(moduleCode), PRIMARY KEY (studentID, moduleCode) ) ''')
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS teachedby(year INTEGER, semester INTEGER, teacherID TEXT, moduleCode TEXT, FOREIGN KEY(teacherID) REFERENCES teacher(teacherID), FOREIGN KEY(moduleCode) REFERENCES module(moduleCode), PRIMARY KEY (teacherID, moduleCode) ) ''')
    crDB.commit()
    cursor.close()

def populateControl():
    # populate table, if table is EMPTY
    crDB = sqlite3.connect('db/crDB.db')
    cc = crDB.cursor()
    cc.execute('SELECT count(*) FROM student')  # count all rows in student table
    isStudentExists = cc.fetchone()[0]
    if isStudentExists == 0:
        populateStudentTable(20)

    cc.execute('SELECT count(*) FROM module')  # count all rows in module table
    isModuleExists = cc.fetchone()[0]
    if isModuleExists == 0:
        populateModuleTable()

    cc.execute('SELECT count(*) FROM teacher')  # count all rows in teacher table
    isTeacherExists = cc.fetchone()[0]
    if isTeacherExists == 0:
        populateTeacherTable(6)

    cc.execute('SELECT count(*) FROM teachedby')  # count all rows in teacher table
    isTeachedbyExists = cc.fetchone()[0]
    if isTeachedbyExists == 0:
        populateTeachedbyTable(7)

    cc.execute('SELECT count(*) FROM grade')  # count all rows in teacher table
    isGradeExists = cc.fetchone()[0]
    if isGradeExists == 0:
        populateGradeTable(7)










