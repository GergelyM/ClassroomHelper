def setAttendanceUI(userID):'''Warning, lots of testing, lots of experimenting to find the best way of doing things as well as'''

import tkinter as tk
from dbHandler import *
import coreFunctionsSQL as core
import sqlite3

#attendanceDB = DbConn("db/crDBv2.db")
attendanceDB = sqlite3.connect("db/crDBv2.db")
connect = attendanceDB.cursor()

studentChecks = []
studentIDs = []
selectedGroupSet = 0

teacherID = userID

#Submit 
def submit():
    #TESTING CODE FOR DUMMY DATA
    '''print("Submit button pressed")
    print(test1.get())
    print(test2.get())
    print(test3.get())
    print(test4.get())
    print(test5.get())'''
    theDate = dateBox.get('1.0','end-1c')
    #print(theDate)
    #connect.execute('INSERT INTO attendance (attendTotal, present, attendDate, studentID, groupsetID) VALUES (0,1,"02/04/17","1733675",9)')
    #connect.execute('DELETE FROM attendance')
    for x in range(0, len(studentChecks)):
        connect.execute('INSERT INTO attendance (attendTotal, present, attendDate, studentID, groupsetID) VALUES (0,?,?,?,?)', [studentChecks[x].get(), theDate, studentIDs[x], selectedGroupSet])            

        #print(str(selectedGroupSet) + ' ' + studentIDs[x] + " " + str(studentChecks[x].get()))
    attendanceDB.commit()
    connect.execute('SELECT * FROM attendance')
    attendance = connect.fetchall()
    print(attendance)

#Searching for students in a given set
def search():
    for widget in frame4.winfo_children():
        widget.destroy()
    del studentChecks[:]
    del studentIDs[:]
    #print("Search button pressed")
    testVar = var.get()
    #print(testVar)
    myIndex = choices.index(testVar)
    #print(myIndex)
    #print(groupSets[myIndex][0])
    global selectedGroupSet
    selectedGroupSet = groupSets[myIndex][0]
    connect.execute('SELECT DISTINCT s.studentID, studentName, studentSurname FROM grade d INNER JOIN student s ON d.studentID=s.studentID WHERE groupsetID=? ORDER BY studentSurname', [selectedGroupSet])
    #connect.execute('SELECT DISTINCT groupsetID, studentID from grade where groupsetID=? ORDER BY studentID', [selectedGroupSet])
    students = connect.fetchall()
    #print(students)
    idx = 0;
    for x in students:
        studentChecks.append(tk.IntVar())
        studentIDs.append(x[0])
        #test1 = tk.IntVar()
        tk.Checkbutton(frame4, text= x[1] + " " + x[2], variable=studentChecks[idx], onvalue=1, offvalue=0).grid(column = 1, row = idx+1)
        print(idx)
        idx += 1
    #print(theMenu.index())
        
#Returns modules teacher teaches for drop down menu
def getModules(teacherID):
    connect.execute('SELECT * FROM groupset WHERE teacherID = ? ORDER BY groupsetID', [teacherID])
    modules = connect.fetchall()
    i = 0 
    for x in modules:
        modules[i] = x[4] + " Set " + x[1]
        i += 1
    return modules

#Eventually returns all students for given groupset
def getGroupSets(teacherID):
    connect.execute('SELECT groupsetID FROM groupset WHERE teacherID = ? ORDER BY groupsetID', [teacherID])
    groupSets = connect.fetchall()
    return groupSets

#UI    
root = tk.Tk()
root.geometry("%dx%d+%d+%d" % (630, 250, 100, 20))
root.title("Attendance Register")
var = tk.StringVar(root)


#UI
frame1 = tk.Frame(root)
frame1.pack()
frame2 = tk.Frame(root)
frame2.pack()
frame3 = tk.Frame(root)
frame3.pack()
frame4 = tk.Frame(root)
frame4.pack()
frame5 = tk.Frame(root)
frame5.pack()

#UI
var.set('Select set')
#teacherID = "st82277" #selected teacher, can be changed for relevant teacherID when connected to main window
choices = getModules(teacherID)
groupSets = getGroupSets(teacherID)
#print(choices[0])
setOption = tk.OptionMenu(frame1, var, *choices)
setOption.pack(side = 'left', padx=5, pady=5)
dateBox = tk.Text(frame2, width = 11, height = 1)
dateBox.pack()
introLabel1 = tk.Label(frame3, text="Student name").grid(column = 1,row = 0)
introLabel2 = tk.Label(frame3, text="Present?").grid(column = 0,row = 0)

#checkCmd = tk.IntVar()
#checkCmd.set(0)

#UI
button1 = tk.Button(frame5, text="Submit", command=submit) # Search button
button1.pack(side='left', padx=5, pady=10) # Asthetic but necessary
button2 = tk.Button(frame1, text="Search", command=search)
button2.pack(side='left')

root.mainloop() # Run 
