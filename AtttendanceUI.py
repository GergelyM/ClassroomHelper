'''Warning, lots of testing, lots of experimenting to find the best way of doing things as well as'''

import tkinter as tk
from dbHandler import *
import coreFunctionsSQL as core

attendanceDB = DbConn("db/crDBv2.db")
connect = attendanceDB.cursor

studentChecks = []
studentIDs = []
selectedGroupSet = 0
    
'''def getStudents(teacherID):
    connect.execute('SELECT * FROM groupset WHERE teacherID = ?', [teacherID])
    groupSets = connect.fetchall()
    #print(len(groupSets))
    i = 0
    #for x in groupSets:        
    details = groupSets[0]
    setInfo = details[1], details[2], details[3], details[4]
    print(setInfo)
    return setInfo

getStudents('st82277')'''

def submit():
    '''print("Submit button pressed")
    #for x in range (1, 7):
     #   ifPresent = "checkCmd" + str(x).get()
      #  print("Student " + x + " has value: " + ifPresent)
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
    connect.execute('SELECT * FROM attendance')
    attendance = connect.fetchall()
    print(attendance)
    
def search():
    for widget in frame4.winfo_children():
        widget.destroy()
    del studentChecks[:]
    del studentIDs[:]
    print("Search button pressed")
    testVar = var.get()
    print(testVar)
    myIndex = choices.index(testVar)
    print(myIndex)
    print(groupSets[myIndex][0])
    global selectedGroupSet
    selectedGroupSet = groupSets[myIndex][0]
    connect.execute('SELECT DISTINCT s.studentID, studentName, studentSurname FROM grade d INNER JOIN student s ON d.studentID=s.studentID WHERE groupsetID=? ORDER BY studentSurname', [selectedGroupSet])
    #connect.execute('SELECT DISTINCT groupsetID, studentID from grade where groupsetID=? ORDER BY studentID', [selectedGroupSet])
    students = connect.fetchall()
    print(students)
    idx = 0;
    for x in students:
        studentChecks.append(tk.IntVar())
        studentIDs.append(x[0])
        #test1 = tk.IntVar()
        tk.Checkbutton(frame4, text= x[1] + " " + x[2], variable=studentChecks[idx], onvalue=1, offvalue=0).grid(column = 1, row = idx+1)
        print(idx)
        idx += 1
    #print(theMenu.index())
        

def getModules(teacherID):
    connect.execute('SELECT * FROM groupset WHERE teacherID = ? ORDER BY groupsetID', [teacherID])
    modules = connect.fetchall()
    i = 0 
    for x in modules:
        modules[i] = x[4] + " Set " + x[1]
        i += 1
    return modules

def getGroupSets(teacherID):
    connect.execute('SELECT groupsetID FROM groupset WHERE teacherID = ? ORDER BY groupsetID', [teacherID])
    groupSets = connect.fetchall()
    return groupSets

    
root = tk.Tk()
root.geometry("%dx%d+%d+%d" % (630, 250, 100, 20))
root.title("Attendance Register")
var = tk.StringVar(root)



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

var.set('Select set')
teacherID = "st82277"
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

'''for x in range (1, 7):
    studentLabel = "label" + str(x)
    studentCheckbox = "checkbox" + str(x)
    print(studentLabel)
    #checkCmd = tk.IntVar()
    #test1 = checkCmd + str(x)
    test1 = tk.IntVar()
    #checkCmd.set(0)
    studentLabel = tk.Label(frame2, text="Student: " + str(x)).grid(column=0,row = x)
    studentCheckbox = tk.Checkbutton(frame2, text="Student: " + str(x), variable=test1, onvalue=1, offvalue=0).grid(column = 1, row = x)
'''


button1 = tk.Button(frame5, text="Submit", command=submit) # Search button
button1.pack(side='left', padx=5, pady=10) # Asthetic but necessary
button2 = tk.Button(frame1, text="Search", command=search)
button2.pack(side='left')

'''test1 = tk.IntVar()
checkbox1 = tk.Checkbutton(frame3, text="Student 1", variable=test1, onvalue=1, offvalue=0).grid(column = 1, row = 1)
test2 = tk.IntVar()
checkbox2 = tk.Checkbutton(frame3, text="Student 2", variable=test2, onvalue=1, offvalue=0).grid(column = 1, row = 2)
test3 = tk.IntVar()
checkbox3 = tk.Checkbutton(frame3, text="Student 3", variable=test3, onvalue=1, offvalue=0).grid(column = 1, row = 3)
test4 = tk.IntVar()
checkbox4 = tk.Checkbutton(frame3, text="Student 4", variable=test4, onvalue=1, offvalue=0).grid(column = 1, row = 4)
test5 = tk.IntVar()
checkbox5 = tk.Checkbutton(frame3, text="Student 5", variable=test5, onvalue=1, offvalue=0).grid(column = 1, row = 5)
'''
root.mainloop() # Run 
