#encoding: UTF-8
#Make sure you're using Python3
#All code is by David, unless otherwise stated
import sqlite3
#connect to the DB (run dBhandler.py first)
conn = sqlite3.connect('db/crDB.db')
c = conn.cursor()

def displayGrades(module): #now displays whose PW is p@assword, working on how to fetch from different tables
    #print contents of all columns for row that match a certain value in a column


    #c.execute('SELECT * FROM student WHERE studentPassword = "p@ssword"')
    c.execute('SELECT * FROM student WHERE studentPassword = ?', [module])

    all_rows = c.fetchall()
    for user in all_rows: #go through all the rows
        print(user[1], '%10s' % user[3], '%13s' % user[4], user[5],) #print selected data with spacing


displayGrades("p@ssword")
