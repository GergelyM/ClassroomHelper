#encoding: UTF-8
#Make sure you're using Python3
#All code is by David, unless otherwise stated


#import sqlite3
from dbHandler import *
#connect to the DB (run dbHandler.py first)
#conn = sqlite3.connect('db/crDB.db')
#c = conn.cursor()
crDB = DbConn("db/crDB.db")
c = crDB.cursor

#Functions
def getModules():
    c.execute('SELECT moduleCode FROM module')
    modules = c.fetchall()
    i = 0 
    for x in modules:
        modules[i] = x[0]
        i += 1
    return modules

def getModuleInfo(module):
    c.execute('SELECT * FROM module WHERE moduleCode = ?', [module]) #Get module deets
    line = c.fetchall()
    deets = line[0] #Select the frist and only tuple in the list
    moduleInfo = deets[1], deets[2], "\n" + deets[3]
    #print(moduleInfo) #print selected data with spacing
    return moduleInfo

def displayGrades(module):
    title = "Getting grades for", module, "..."
    #print("Getting grades for", module, "...")
    #print('%15s' % "Student ID",  '%15s' % "Name", '%13s' % "Surname", '%15s' % "DoB", '%10s' % "Grade") #Print header
    header = '%15s' % "Student ID",  '%15s' % "Name", '%13s' % "Surname", '%15s' % "DoB", '%10s' % "Grade"
    c.execute('SELECT * FROM grade WHERE moduleCode = ?', [module]) #Get grades
    allGrades = c.fetchall()
    moduleList = []
    for grade in allGrades: #go through all the rows
        studentId = grade[3] #Find the student ID
        c.execute('SELECT * FROM student WHERE studentId = ?', [studentId]) #Get student deets
        line = c.fetchall()
        user = line[0] #Select the frist and only tuple in the list
        #print('%15s' % user[1], '%15s' % user[3], '%13s' % user[4], '%15s' % user[5], '%10s' % grade[0]) #print selected data with spacing
        moduleItem = '%15s' % user[1], '%15s' % user[3], '%13s' % user[4], '%15s' % user[5], '%10s' % grade[0]
        moduleList.append(moduleItem)
    return (title, header, moduleList)
        
def displayModules(teacher):
    c.execute('SELECT * FROM teacher WHERE teacherID = ?', [teacher]) #Get teacher info
    line = c.fetchall() #[0]?
    user = line[0] #Select the first and only tuple in the list
    title = "Getting your modules, ", user[2],  user[3], user[4], "..."
    header = '%15s' % "Module Code",  '%15s' % "Module Name", '%13s' % "Module Desc."
    c.execute('SELECT moduleCode FROM teachedby WHERE teacherID = ?', [teacher]) #Get modules
    modules = c.fetchall()
    i = 0 
    for x in modules:
        modules[i] = x[0]
        i += 1
    #maybe would be lucky to use the normal # comments, the ''' normally used for other kind of comments, although it works
    '''
    ALTERNATIVE:
    i = 0
    while (i < len(modules)):
        modules[i] = modules[i][0]
        i+=1
    '''
    moduleList = []
    for module in modules:
        c.execute('SELECT * FROM module WHERE moduleCode = ?', [module]) #Get modules
        line = c.fetchall()
        mod = line[0][1:]
        moduleList.append(mod)
    #print(moduleList)
    #Example: [('M01001', 'Art of nothing', 'Nobody helped me out, so no description, you write better if you want'), ...]
    
    return title, header, moduleList

def diplayMyGrades(student): #TODO David
    return 0
    
#TODO-David Teacher navigation between modules summary, single module, attendance, 

#TESTING:
#getModuleInfo("M03010")
#displayGrades("M03010")
#displayModules("st144228203")
#getModules()
'''
#when you'll write this code, consider that the grades will add up from three values, wighted. see Hassan's specs.
DO NOT REMOVE
First attempt: DEPRECATED.
Leave for reference. Thanks. David.
def displayGrades(module): #now displays whose PW is p@assword, working on how to fetch from different tables
    #print contents of all columns for row that match a certain value in a column

    #c.execute('SELECT * FROM student WHERE studentPassword = "p@ssword"')
    c.execute('SELECT * FROM student WHERE studentPassword = ?', [module]) #Thanks Gary for the fix

    all_rows = c.fetchall()
    for user in all_rows: #go through all the rows
        print(user[1], '%10s' % user[3], '%13s' % user[4], user[5],) #print selected data with spacing
'''
