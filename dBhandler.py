#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from tinydb import Query
from tinydb import TinyDB
from datetime import *


#check and create db

def checkDB () :
    return


if __name__ == "__main__":
    
    
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
    #studentID generator: 
    
    def genStdNum(name, surname, dateOfBirth):
        print(date.today())
    
    
    genStdNum("name", "surname", "dateOfBirth")