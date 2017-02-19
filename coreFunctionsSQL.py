#encoding: UTF-8
#Make sure you're using Python3
#All code is by David, unless otherwise stated
import sqlite3
#connect to the DB (run dBhandler.py first)
conn = sqlite3.connect('db/crDB.db')
c = conn.cursor()
def getModuleInfo(module):
    c.execute('SELECT * FROM module WHERE moduleCode = ?', [module]) #Get module deets
    line = c.fetchall()
    deets = line[0] #Select the frist and only tuple in the list
    print(deets[1], deets[2], "\n" + deets[3]) #print selected data with spacing

def displayGrades(module):
    print("Getting grades for", module, "...")
    print('%15s' % "Student ID",  '%15s' % "Name", '%13s' % "Surname", '%15s' % "DoB", '%10s' % "Grade") #Print header
    c.execute('SELECT * FROM grade WHERE moduleCode = ?', [module]) #Get grades
    allGrades = c.fetchall()
    for grade in allGrades: #go through all the rows
        studentId = grade[3] #Find the student ID
        c.execute('SELECT * FROM student WHERE studentId = ?', [studentId]) #Get student deets
        line = c.fetchall()
        user = line[0] #Select the frist and only tuple in the list
        print('%15s' % user[1], '%15s' % user[3], '%13s' % user[4], '%15s' % user[5], '%10s' % grade[0]) #print selected data with spacing
        



getModuleInfo("M02001")
displayGrades("M02001")

'''
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
