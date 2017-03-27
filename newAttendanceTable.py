# add new field to attendance table
# new field called: present

import sqlite3

def reworkAttendanceTable():

    cursor.execute('drop table if exists attendance')  # this works
    print("Table 'attendance' dropped")
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS attendance(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            attendTotal INTEGER,
            present INTEGER,
            attendDate TEXT,
            studentID TEXT,
            groupsetID INTEGER,
            FOREIGN KEY(studentID) REFERENCES student(studentID),
            FOREIGN KEY(groupsetID) REFERENCES groupset(groupsetID) ) ''')

    print("New 'attendance' table created")

    cursor.execute("PRAGMA table_info('attendance') ")
    dataFetch = cursor.fetchall()
    print("Table: attendance // PRAGMA:")
    for item in dataFetch:
        print(str(item[0]) + " - Field name: " + str(item[1]) + " / Type: " + str(item[2]))

connection = sqlite3.connect("db/crDBv2.db")
cursor = connection.cursor()

reworkAttendanceTable()
connection.commit()
