#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from tinydb import Query
from tinydb import TinyDB
from datetime import *


#check and create db
#TODO-Gary check if folder exist, create one if not
#TODO-Gary check if the file exists, catch exceptions, I think the basic code does it anyway
def commitDB ():
    #not used yet
    return

#create the main DB for our project
crDB = TinyDB('./db/crDB.json')
print("just passed create/reach DB")

#create and update tables. They behave just the same as the TinyDB class.
#table = db.table('name')
#table.insert({'value': True})
#table.all()
#[{'value': True}]

#remove a table
#db.purge_table('table_name')

#list with the names of all tables
#db.tables()

tableStudent = crDB.table('STUDENT')
tableTeacher = crDB.table('TEACHER')
tableGrade = crDB.table('GRADE')
tableModule = crDB.table('MODULE')
tableTeachedBy = crDB.table('TEACHEDBY')

tableStudent.insert({'studentID':'161015234567',
                    'studentSurname':'Smith',
                    'studentName':'John',
                    'studentDateOfBirth':'02-12-1999',
                    'password':'p@ssword'})

#TODO-Gary write a generic, unique userID generator
#use given data find in DB: initials, date of birth, and current date
def genStdNum(name, surname, dateOfBirth):
    currentYear = date.today().strftime("%y") #this gives back the current year in 2-digit format
    fInitial = ord(name[0])
    sInitial = ord(surname[0])
    dof = dateOfBirth.split("-")
    dof[2] = dof[2].strftime("%y")


    #add things up
    uniqueID = "%s%s%s%s%s" % (currentYear,fInitial+sInitial,dof[0],dof[1],dof[2])
    print(uniqueID)

