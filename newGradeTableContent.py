#import sqlite3
#from random import randint
#import dbHandler

#####################################################################
#
# WARNING! DO NOT RUN THIS FILE FOR YOUR OWN GOOD!
#
#####################################################################


def populateGradeTable():
    # grade table should have records as many as students / modules.
    # each student will have more than one groupset (aka. module), and each groupset will give one grade to each student
    # each student can be signed off to one groupset/module
    # students will have 4-6 modules per semester therefore will have 4-6 grades per semester

    # cursor.execute('drop table if exists grade;') # this works
    #
    # cursor.execute(
    #     '''CREATE TABLE IF NOT EXISTS grade(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     grade INTEGER,
    #     gradeType TEXT,
    #     studentID TEXT,
    #     groupsetID INTEGER,
    #     FOREIGN KEY(studentID) REFERENCES student(studentID),
    #     FOREIGN KEY(groupsetID) REFERENCES groupset(groupsetID) ) ''')
    # connection.commit()

    c5 = cursor
    c6 = cursor
    #fetch all student IDs
    c5.execute('SELECT studentID FROM student')
    allStudentID = c5.fetchall()
    print(allStudentID)
    #fetch all groupset IDs
    c5.execute('SELECT groupsetID FROM groupset')
    allgroupsetID = c5.fetchall()
    grade = 0

    for student in allStudentID:
        dataPush = []
        #tuple[0] #actual studentID
        #random groupset id
        #gradeType <A = assignment> or <E = exam>
        newRand = randint(0, len(allgroupsetID) -1)
        randomGroupsetID = allgroupsetID[newRand][0]
        dataPush.append( (grade, "assignment", student[0], randomGroupsetID) )
        dataPush.append( (grade, "exam", student[0], randomGroupsetID) )
        dataPush.append( (grade, "attendance", student[0], randomGroupsetID) )
        print(dataPush)
        c6.executemany( 'INSERT INTO grade (grade, gradeType, studentID, groupsetID) VALUES (?,?,?,?)', dataPush )

    cursor.execute("SELECT * FROM grade")
    testQuery = cursor.fetchall()
    print(testQuery)
    for item in testQuery:
        print(item)

# build DB connection
# connection = dbHandler.DbConn("db/crDBv2.db")
# crDB = connection
# cursor = connection.cursor

connection = sqlite3.connect("db/crDBv2.db")
cursor = connection.cursor()

populateGradeTable()
connection.commit()
