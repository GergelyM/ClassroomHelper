####################################################################################
#
# You * MUST NOT * run this script!
# If you do so it will overwrite your DB file with an empty version of it.
# You are welcome to read it if you need more info of the structure or
# the how-to of the table population functions. There are files missing
# from this GIT repo. to prevent complete run of this script.
#
####################################################################################

import sqlite3
import time
import os
from random import randint
import dbHandler
import randomIdGenerator

# check and create db
def initDB():
    if not os.path.isdir("./db"):  # if this won't work well use os.path.exists(<path>)
        print("No 'db' folder. Create folder. ")
        os.makedirs("./db")  # at this level of the project it should just rely on an existing DB on path
        createDB = sqlite3.connect('db/crDBv2.db')
    elif not os.path.isfile("./db/crDBv2.db"):
        print("No 'crDBv2.db' file. Create file.")
        createDB = sqlite3.connect('db/crDBv2.db')
    else:
        print("Folder and file present. Connect db.")
        createDB = sqlite3.connect('db/crDBv2.db')
    return createDB

def createTables():
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS student(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            studentID TEXT UNIQUE,
            studentGender TEXT,
            studentSurname TEXT,
            studentName TEXT,
            studentEmail TEXT,
            studentPassword TEXT) ''')
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS teacher(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacherID TEXT UNIQUE,
            teacherTitle TEXT,
            teacherSurname TEXT,
            teacherName TEXT,
            teacherEmail TEXT,
            teacherPassword TEXT) ''')
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS module(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            moduleCode TEXT UNIQUE,
            moduleName TEXT,
            moduleDescription TEXT ) ''')
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS groupset(
            groupsetID INTEGER PRIMARY KEY AUTOINCREMENT,
            groupsetName TEXT,
            year TEXT,
            semester INTEGER,
            moduleCode TEXT,
            teacherID TEXT,
            FOREIGN KEY (moduleCode) REFERENCES module(moduleCode),
            FOREIGN KEY (teacherID) REFERENCES teacher(teacherID) )''')
    cursor.execute(
            '''CREATE TABLE IF NOT EXISTS grade(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grade INTEGER,
            gradeType TEXT,
            studentID TEXT,
            groupsetID INTEGER,
            FOREIGN KEY(studentID) REFERENCES student(studentID),
            FOREIGN KEY(groupsetID) REFERENCES groupset(groupsetID) ) ''')
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS attendance(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            attendTotal INTEGER,
            attendDate TEXT,
            studentID TEXT,
            groupsetID INTEGER,
            FOREIGN KEY(studentID) REFERENCES student(studentID),
            FOREIGN KEY(groupsetID) REFERENCES groupset(groupsetID) ) ''')

def generateRandomPerson(role):
    lastNameFile = open("teststuff/lastNames.txt","r")
    girlNameFile = open("teststuff/girlNames.txt","r")
    boyNameFile = open("teststuff/boyNames.txt","r")
    lastNameList = lastNameFile.readlines()
    lastNameFile.close()
    girlNameList = girlNameFile.readlines()
    girlNameFile.close()
    boyNameList = boyNameFile.readlines()
    boyNameFile.close()
    randGender = randint(0,1)
    randLast = randint(0, len(lastNameList)-1)
    lastName = lastNameList[randLast].strip()
    if randGender == 0: #male
        randSur = randint(0, len(boyNameList)-1)
        firstName = boyNameList[randSur].strip()
        gender = "male"
        title = "Mr"
    else:   #female
        randSur = randint(0, len(girlNameList) - 1)
        firstName = girlNameList[randSur].strip()
        gender = "female"
        title = "Ms"
    if role == "student" :
        randomUser = ( randomIdGenerator.oneNewStudentId(), gender, lastName, firstName,"","p@ssword" )
    elif role == "teacher":
        randomUser = (randomIdGenerator.oneNewTeacherId(), title, lastName, firstName,"","p@ssword")
    return randomUser

def populateStudentTable(x):
    studentBatch = []
    i=0
    while (i <= x):
        studentBatch.append(generateRandomPerson("student"))
        i += 1
    cursor2 = cursor
    cursor2.executemany(
        'INSERT INTO student(studentID, studentGender, studentSurname, studentName, studentEmail, studentPassword) VALUES (?,?,?,?,?,?)',
        studentBatch)

def populateTeacherTable(x):
    teacherBatch = []
    i = 0
    while (i <= x):
        teacherBatch.append(generateRandomPerson("teacher"))
        i += 1
    cursor2 = cursor
    cursor2.executemany(
        'INSERT INTO teacher(teacherID, teacherTitle, teacherSurname, teacherName, teacherEmail, teacherPassword) VALUES (?,?,?,?,?,?)',
        teacherBatch)

def randLine():
    sentenceFile = open("teststuff/sentences.txt", "r")
    sentenceList = sentenceFile.readlines()
    rand = randint(0, len(sentenceList) - 1)
    return sentenceList[rand].strip()

def populateModuleTable(moduleCode):
    moduleNameFile = open("teststuff/moduleNames.txt", "r")
    moduleNameList = moduleNameFile.readlines()
    loopControl = 1
    existingModuleNames = []
    while loopControl == 1:
        randModuleName = randint(0, len(moduleNameList) - 1)
        cursor.execute('''SELECT moduleName FROM module''')
        tempModNameList = cursor.fetchall()
        for tup in tempModNameList:
            existingModuleNames.append(tup[0])
        thisModuleName = moduleNameList[randModuleName].strip()
        if thisModuleName not in existingModuleNames:
            loopControl = 0
    newModule = ( moduleCode, thisModuleName, randLine() )
    cursor3 = cursor
    cursor3.execute('''INSERT INTO module(moduleCode, moduleName, moduleDescription) VALUES (?,?,?)''', newModule)

def populateGroupsetTable(moduleID):
    # this must be exactly as many as modules we have in default
    # because by design every module have at least one set, or more if needed
    # therefore it should be called every time after adding new modules,
    # otherwise it will not be possible to add students to the module

    cursor2 = cursor
    cursor3 = cursor
    cursor2.execute(''' SELECT teacherID FROM teacher ORDER BY random() LIMIT 1 ''')
    ranTeacher = cursor2.fetchone()[0]
    gradeSemester = randint(1, 2)
    gradeYear = time.strftime("%Y")  # 4 digit year
    dataPush = ("a", gradeYear, gradeSemester, moduleID, ranTeacher)
    cursor3.execute(''' INSERT INTO groupset (groupsetName, year, semester, moduleCode, teacherID) VALUES (?,?,?,?,?)''', dataPush)


def populateGradeTable():
    # grade table should have records as many as students / modules.
    # each student will have more than one groupset (aka. module), and each groupset will give one grade to each student
    # each student can be signed off to one groupset/module
    # students will have 4-6 modules per semester therefore will have 4-6 grades per semester

    c5 = cursor
    c6 = cursor
    #fetch all student IDs
    c5.execute('SELECT studentID FROM student')
    allStudentID = c5.fetchall()
    #fetch all groupset IDs
    c5.execute('SELECT groupsetID FROM groupset')
    allgroupsetID = c5.fetchall()
    grade = 0

    for tuple in allStudentID:
        #tuple[0] #actual studentID
        #random groupset id
        #gradeType <A = assignment> or <E = exam>
        newRand = randint(0, len(allgroupsetID) -1)
        randomGroupsetID = allgroupsetID[newRand][0]
        dataPush = (grade, "A", tuple[0], randomGroupsetID)
        c6.execute( 'INSERT INTO grade(grade, gradeType, studentID, groupsetID) VALUES (?,?,?,?)', dataPush )


#get some sample data out of the DB
def testQueries():
    #do some test queries from
    c = crDB.cursor
 # 1
    #c.execute('SELECT * FROM student ORDER BY random() LIMIT 5')
    c.execute('SELECT * FROM student')
    allRows = c.fetchall()
    print("\nAll records from 'student' table")
    print("id, studentID, studentGender, studentSurname, studentName, studentEmail, studentPassword")
    for row in allRows:
        print(row)
 # 2
    #c.execute('SELECT * FROM teacher ORDER BY random() LIMIT 5')
    c.execute('SELECT * FROM teacher')
    allRows = c.fetchall()
    print("\nAll records from 'teacher' table")
    print("id, teacherID, teacherTitle, teacherSurname, teacherName, teacherEmail, teacherPassword")
    for row in allRows:
        print(row)
 # 3
    #c.execute('SELECT * FROM module ORDER BY random() LIMIT 5')
    c.execute('SELECT * FROM module')
    allRows = c.fetchall()
    print("\nAll records from 'module' table")
    print("id, moduleCode, moduleName, moduleDescription")
    for row in allRows:
        print(row)
 # 4
    #c.execute('SELECT * FROM groupset ORDER BY random() LIMIT 5')
    c.execute('SELECT * FROM groupset')
    allRows = c.fetchall()
    print("\nAll records from 'groupset' table")
    print("id, groupsetName, year, semester, moduleCode, teacherID")
    for row in allRows:
        print(row)
 # 5
    #c.execute('SELECT * FROM grade ORDER BY random() LIMIT 5')
    c.execute('SELECT * FROM grade')
    allRows = c.fetchall()
    print("\nAll records from 'grade' table")
    print("id, grade, gradeType, studentID, groupsetID")
    for row in allRows:
        print(row)
    # sample output as is
    print("\nSample raw output:")
    print(allRows)
    print("\n")

#######################################################################################

# crate and populate tables
# print( initDB() )

# build DB connection
connection = dbHandler.DbConn("db/crDBv2.db")
crDB = connection
cursor = connection.cursor

createTables()
# populate FIRST
populateStudentTable(50)
# SECOND
populateTeacherTable(10)

moduleCodeList = ["M01001", "M01003", "M02001", "M03001", "M03010", "M03011", "M03012", "M02013", "M02014", "M04001", "M04002"]
# THIRD
for code in moduleCodeList:
    populateModuleTable(code)
# FOURTH
for module in moduleCodeList:
    populateGroupsetTable(module)
# FIFTH
populateGradeTable()
# c5.execute('SELECT * FROM grade WHERE groupsetID=:Id', {"Id" : 1})
# allgrade = c5.fetchall()
# print(allgrade)
# SIXTH
# attendance not yet populated

#print out all data from DB
testQueries()


