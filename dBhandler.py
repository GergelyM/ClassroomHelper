#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#FCK tinyDB, ditched for good, too complicated to be "small and easy"

import sqlite3
from datetime import *
import os
from random import randint


#check and create db
#renamed to fit better to SqLite
def checkNcreateDB():
    #as 15-02 12:00 it is fully functional on Ubuntu 16.04
    if not os.path.isdir("./db") :
        os.makedirs("./db")
        crDB = sqlite3.connect('db/crDB')
        # cursor = crDB.cursor()   needed to interact with the DB
        cursor = crDB.cursor()
        # simplified version no contact details saved now
        # cursor.execute('''CREATE TABLE student( id INTEGER PRIMARY KEY AUTOINCREMENT, studentID TEXT UNIQUE, studentTitle TEXT, studentName TEXT, studentSurname TEXT, studentDateOfBirth TEXT, studentPhone TEXT, studentEmail TEXT UNIQUE, studentPassword TEXT) ''')
        cursor.execute(
            '''CREATE TABLE student( id INTEGER PRIMARY KEY AUTOINCREMENT, studentID TEXT UNIQUE, studentTitle TEXT, studentName TEXT, studentSurname TEXT, studentDateOfBirth TEXT, studentPassword TEXT) ''')
        # cursor.execute('''CREATE TABLE teacher( id INTEGER PRIMARY KEY AUTOINCREMENT, teacherID TEXT UNIQUE, teacherTitle TEXT, teacherName TEXT, teacherSurname TEXT, teacherPhone TEXT, teacherEmail TEXT UNIQUE, teacherPassword TEXT) ''')
        cursor.execute(
            '''CREATE TABLE teacher( id INTEGER PRIMARY KEY AUTOINCREMENT, teacherID TEXT UNIQUE, teacherTitle TEXT, teacherName TEXT, teacherSurname TEXT, teacherPassword TEXT) ''')
        cursor.execute(
            '''CREATE TABLE module( id INTEGER PRIMARY KEY AUTOINCREMENT, moduleCode TEXT UNIQUE, moduleName TEXT, moduleDescription TEXT ) ''')
        cursor.execute(
            '''CREATE TABLE grade(grade INTEGER, year INTEGER, semester INTEGER, studentID TEXT, moduleCode TEXT, FOREIGN KEY(studentID) REFERENCES student(studentID), FOREIGN KEY(moduleCode) REFERENCES module(moduleCode), PRIMARY KEY (studentID, moduleCode) ) ''')
        cursor.execute(
            '''CREATE TABLE teachedby(year INTEGER, semester INTEGER, teacherID TEXT, moduleCode TEXT, FOREIGN KEY(teacherID) REFERENCES teacher(teacherID), FOREIGN KEY(moduleCode) REFERENCES module(moduleCode), PRIMARY KEY (teacherID, moduleCode) ) ''')
        crDB.commit()
    else:
        crDB = sqlite3.connect('db/crDB')
    return crDB

#create the main DB for our project
crDB = checkNcreateDB()

# #TODO-Gary do this only if no tables present, check for table presence
# tableStudent = crDB.table('STUDENT')
# tableTeacher = crDB.table('TEACHER')
# tableGrade = crDB.table('GRADE')
# tableModule = crDB.table('MODULE')
# tableTeachedBy = crDB.table('TEACHEDBY')

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
def generateRandomStudent(randomStudent=None):
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
    genStdID = genIdNum(name[randOne], surname[randTwo], allDates[randThree], "student")
    # id, studentID TEXT, studentTitle TEXT, studentName TEXT, studentSurname TEXT, studentDateOfBirth TEXT, studentPassword TEXT
    randomStudent = ( genStdID,"",name[randOne],surname[randTwo],allDates[randThree],"p@ssword" )
    return randomStudent

#TODO-Gary check if studentID exist in DB
#TODO-Gary check and add real password later
#renamed to reflect is function better from: insertXRndStudent(x) to populateStudentTable(x)
def populateStudentTable(x):
    # # check if table exists already //DONE
    # if ("STUDENT" not in crDB.tables()):
    #     global tableModule  # to make sure we use the same variable if it needed to use here
    #     tableModule = crDB.table('STUDENT')
    studentBatch = []
    i=0
    while (i <= x):
        studentBatch.append(generateRandomStudent())
        i += 1
    #tableStudent.insert({'studentID': dataIn[3],'studentSurname': dataIn[1],'studentName': dataIn[0],'studentDateOfBirth': dataIn[2],'password': 'p@ssword'})
    cursor2 = crDB.cursor()
    cursor2.executemany('INSERT INTO student(studentID, studentTitle, studentName, studentSurname, studentDateOfBirth, studentPassword) VALUES (?,?,?,?,?,?)', studentBatch)
    crDB.commit()
    # maybe need the attribute names in () after the table name

    #maybe it should return with a True on success
    #exception handling would be a good solution (try/except)


def populateModuleTable():
    #check if table exists already //DONE
    # if ("MODULE" not in crDB.tables()):
    #     global tableModule      #to make sure we use the same variable if it needed to use here
    #     tableModule = crDB.table('MODULE')
    #TODO-Gary create an algorithm generates module uniqueID, eid could be used for that
    #TODO-Gary describe modulecode //DONE
    #moduleCode: M + 2digit + 3digit -> M01001, M02005, M01010
    #tableModule.insert({'moduleID': dataIn[3],'moduleCode': dataIn[1],'moduleName': dataIn[0],'moduleDescription': dataIn[2]})
    # controlCheck = Query()
    # test = crDB.search(controlCheck.MODULE.moduleID == "004")
    # print(test)
    # tableModule.insert({'moduleID': "0001",'moduleCode': "M01001",'moduleName': "Idontknow",'moduleDescription': "Nobody helped me out, so no description, you write better if you want"})
    # tableModule.insert({'moduleID': "0002",'moduleCode': "M01003",'moduleName': "NoModulenames",'moduleDescription': "Nobody helped me out, so no description, you write better if you want"})
    # tableModule.insert({'moduleID': "0003",'moduleCode': "M02001",'moduleName': "StillIdontknow",'moduleDescription': "Nobody helped me out, so no description, you write better if you want"})
    # tableModule.insert({'moduleID': "0004",'moduleCode': "M03010",'moduleName': "Yeaaah",'moduleDescription': "Nobody helped me out, so no description, you write better if you want"})
    # tableModule.insert({'moduleID': "0005",'moduleCode': "M03010",'moduleName': "Yeaaah",'moduleDescription': "Nobody helped me out, so no description, you write better if you want"})
    # tableModule.insert({'moduleID': "0006",'moduleCode': "M03011",'moduleName': "Yeaaah",'moduleDescription': "Nobody helped me out, so no description, you write better if you want"})
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

#some tinyDB bs removed, mostly comments

#populate student and module table, if table is EMPTY
cc = crDB.cursor()
cc.execute('SELECT count(*) FROM student') #count all rows in student table
isStudentExists = cc.fetchone()[0]
if isStudentExists == 0 :
    populateStudentTable(20)
else:
    print("superb")
cc.execute('SELECT count(*) FROM student') #count all rows in module table
isModuleExists = cc.fetchone()[0]
if isModuleExists == 0:
    populateModuleTable()
else:
    print("awesome")




#do some test queries from
c = crDB.cursor()
c.execute('SELECT * FROM module')
allRows = c.fetchall()
for row in allRows:
    print(row)
