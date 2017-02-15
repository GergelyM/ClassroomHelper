#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#some hints for tinyDB usage
#create and update tables. They behave just the same as the TinyDB class.
#table = db.table('name')
#table.insert({'value': True})
#table.all()
#>>> [{'value': True}]

#remove a table
#db.purge_table('table_name')

#list with the names of all tables
#db.tables()

from tinydb import where
from tinydb import Query
from tinydb import TinyDB
from datetime import *
import os
from random import randint

#check and create db
def commitDB ():
    #as 15-02 12:00 it is fully functional on linux
    if not os.path.isdir("./db") :
        os.makedirs("./db")
        db = TinyDB('./db/crDB.json')
    else:
        db = TinyDB('./db/crDB.json')
    return db

#create the main DB for our project
crDB = commitDB()

#if ("STUDENT" in crDB.tables()):
#    print("yes")

#TODO-Gary do this only if no tables present, check for table presence
tableStudent = crDB.table('STUDENT')
tableTeacher = crDB.table('TEACHER')
tableGrade = crDB.table('GRADE')
tableModule = crDB.table('MODULE')
tableTeachedBy = crDB.table('TEACHEDBY')

#TODO-Gary write a generic, unique userID generator // DONE for students
#use given data find in DB: initials, date of birth, and current date
def genStdNum(name, surname, dateOfBirth,role):
    currentYear = date.today().strftime("%y") #this gives back the current year in 2-digit format
    fInitial = ord(name[0])
    sInitial = ord(surname[0])
    dof = dateOfBirth.split("/")    #the correct date format: dd/mm/yyyy
    dof[2]=dof[2][-2::]
    if role == "student" :
        uniqueID = "%s%s%s%s%s" % (currentYear, fInitial + sInitial, dof[0], dof[1], dof[2])
    elif role == "teacher":
        uniqueID = "%s%s%s%s%s" % ("st", fInitial + sInitial, dof[0], dof[1], dof[2])
    else:
        uniqueID = "%s%s%s%s%s" % (currentYear, fInitial + sInitial, dof[0], dof[1], dof[2])
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
    genStdID = genStdNum(name[randOne],surname[randTwo],allDates[randThree],"student")
    randomStudent = [ name[randOne],surname[randTwo],allDates[randThree],genStdID  ]
    return randomStudent

#TODO-Gary check if studentID exist
#TODO-Gary check and add real password later
def insertXRndStudent(x):
    # check if table exists already //DONE
    if ("STUDENT" not in crDB.tables()):
        global tableModule  # to make sure we use the same variable if it needed to use here
        tableModule = crDB.table('STUDENT')
    i=0
    while (i <= x):
        dataIn = generateRandomStudent()
        tableStudent.insert({'studentID': dataIn[3],'studentSurname': dataIn[1],'studentName': dataIn[0],'studentDateOfBirth': dataIn[2],'password': 'p@ssword'})
        i += 1
    #maybe it should return with a True on success
    #exception handling would be a good solution (try/except)


#print(tableStudent.all())

def populateModuleTable():
    #check if table exists already //DONE
    if ("MODULE" not in crDB.tables()):
        global tableModule      #to make sure we use the same variable if it needed to use here
        tableModule = crDB.table('MODULE')
    #TODO-Gary create an algorithm generates module uniqueID, eid could be used for that
    #TODO-Gary describe modulecode //DONE
    #moduleCode: M + 2digit + 3digit -> M01001, M02005, M01010
    #tableModule.insert({'moduleID': dataIn[3],'moduleCode': dataIn[1],'moduleName': dataIn[0],'moduleDescription': dataIn[2]})
    # controlCheck = Query()
    # test = crDB.search(controlCheck.MODULE.moduleID == "004")
    # print(test)
    tableModule.insert({'moduleID': "0001",'moduleCode': "M01001",'moduleName': "Idontknow",'moduleDescription': "Nobody helped me out, so no description, you write better if you want"})
    tableModule.insert({'moduleID': "0002",'moduleCode': "M01003",'moduleName': "NoModulenames",'moduleDescription': "Nobody helped me out, so no description, you write better if you want"})
    tableModule.insert({'moduleID': "0003",'moduleCode': "M02001",'moduleName': "StillIdontknow",'moduleDescription': "Nobody helped me out, so no description, you write better if you want"})
    tableModule.insert({'moduleID': "0004",'moduleCode': "M03010",'moduleName': "Yeaaah",'moduleDescription': "Nobody helped me out, so no description, you write better if you want"})
    tableModule.insert({'moduleID': "0005",'moduleCode': "M03010",'moduleName': "Yeaaah",'moduleDescription': "Nobody helped me out, so no description, you write better if you want"})
    tableModule.insert({'moduleID': "0006",'moduleCode': "M03011",'moduleName': "Yeaaah",'moduleDescription': "Nobody helped me out, so no description, you write better if you want"})
    # maybe it should return with a True on success
    # exception handling would be a good solution (try/except)

#crDB.purge_table('MODULE')
#populateModuleTable()
#print(tableModule.all())

ququ = Query ()
#wtf = crDB.search(ququ.moduleCode == 'M03010')
wtf = tableModule.all()


#wtf = crDB.table('MODULE').all()[0].keys()
#wtf = crDB.table('MODULE').search(where('moduleID') == '0001')
#wtf = crDB.table('MODULE').search(where('moduleCode') == 'M03010')
print(wtf)
#print(tableModule.all())
