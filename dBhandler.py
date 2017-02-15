#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

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

#some hint for tinyDB usage
#create and update tables. They behave just the same as the TinyDB class.
#table = db.table('name')
#table.insert({'value': True})
#table.all()
#[{'value': True}]

#remove a table
#db.purge_table('table_name')

#list with the names of all tables
#db.tables()

#TODO-Gary do this only if no tables present, check for table presence
tableStudent = crDB.table('STUDENT')
tableTeacher = crDB.table('TEACHER')
tableGrade = crDB.table('GRADE')
tableModule = crDB.table('MODULE')
tableTeachedBy = crDB.table('TEACHEDBY')




#TODO-Gary write a generic, unique userID generator
#use given data find in DB: initials, date of birth, and current date
def genStdNum(name, surname, dateOfBirth):
    currentYear = date.today().strftime("%y") #this gives back the current year in 2-digit format
    fInitial = ord(name[0])
    sInitial = ord(surname[0])
    dof = dateOfBirth.split("/")    #the correct date format: dd/mm/yyyy
    dof[2]=dof[2][-2::]

    #add things up
    uniqueID = "%s%s%s%s%s" % (currentYear,fInitial+sInitial,dof[0],dof[1],dof[2])
    return uniqueID

#TODO-Gary add comments to this function
#should be committed
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
    genStdID = genStdNum(name[randOne],surname[randTwo],allDates[randThree])
    randomStudent = [ name[randOne],surname[randTwo],allDates[randThree],genStdID  ]
    return randomStudent

#print(generateRandomStudent())
#generate and insert complete student detail using generateRandomStudent() and generate genStdNum()

def insertXRndStudent(x):
    i=0
    while (i <= x):
        dataIn = generateRandomStudent()
        #TODO-Gary check if studentID exist
        #TODO-Gary check and add real password later
        #print('studentID: '+ dataIn[3]+' \t studentSurname: '+ dataIn[1]+' \t studentName: '+ dataIn[0]+' \t studentDateOfBirth: '+ dataIn[2]+' \t password: '+ 'p@ssword')
        tableStudent.insert({'studentID': dataIn[3],'studentSurname': dataIn[1],'studentName': dataIn[0],'studentDateOfBirth': dataIn[2],'password': 'p@ssword'})
        i += 1
    #print("insert random students was successful")

#insertXRndStudent(20)
#print(tableStudent.all())

#generateRandomStudent()
