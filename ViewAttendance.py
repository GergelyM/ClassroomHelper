from tkinter import *
from dbHandler import *
from studentViewUI import *
from TeacherViewOneStudentsGrades import *

# Window that is placed in the display frame, has a top frame for drop down menus and a bottom frame for the display
class Window(object):

    crDB = DbConn("db/crDBv2.db")
    c = crDB.cursor

    def __init__(self, teacher, mainFrame):
        self.mainFrame = mainFrame
        self.teacher = teacher
        self.grade = []
        self.topFrame = Frame(self.mainFrame, bg="chartreuse3")
        self.topFrame.pack(fill=X, expand=1, side=TOP, anchor=N)
        self.bottomFrame = Frame(self.mainFrame, bg="snow")
        self.bottomFrame.pack(fill=X, expand=1, side=BOTTOM, anchor=N)

    # Creates two drop down menus and 2 search buttons in the menu frame. The first used for selecting a set and the
    # second for selecting a date. First menu must be 'searched' in order for dates to show in the second
    def displayonestudentview(self):
        self.dates = ["NONE"]
        self.var = StringVar(self.topFrame)
        self.var.set("Select Set")
        self.menu = OptionMenu(self.topFrame, self.var, *self.teacher.sets)
        self.menu.pack(side=LEFT, anchor=N, padx=10, pady=10)
        self.search = Button(self.topFrame, text="Search", command=self.search2, relief=GROOVE)
        self.search.pack(side="left", padx=10, pady=10, anchor=N)
        self.var2 = StringVar(self.topFrame)
        self.var2.set("Select Date")
        self.menu = OptionMenu(self.topFrame, self.var2, *self.dates)
        self.menu.pack(side="left", anchor=N, padx=10, pady=10)
        self.search = Button(self.topFrame, text="Search", command=self.search3, relief=GROOVE)
        self.search.pack(side="left", padx=10, pady=10, anchor=N)

    # Finds all the dates the selected set had a class
    def search2(self):

        self.set = self.var.get()
        self.c.execute("SELECT attendDate FROM attendance WHERE groupsetID = '" + self.set[1] + "'")
        self.dates = self.c.fetchall()
        self.dates = list(set(self.dates))
        self.menu.pack_forget()
        self.search.pack_forget()
        self.menu = OptionMenu(self.topFrame, self.var2, *self.dates)
        self.menu.pack(side="left", anchor=N, padx=10, pady=10)
        self.search = Button(self.topFrame, text="Search", command=self.search3, relief=GROOVE)
        self.search.pack(side="left", padx=10, pady=10, anchor=N)


    # Finds all the students who did or did not attend that class
    def search3(self):
        self.date = self.var2.get()
        self.date = str(self.date[2:10])
        self.c.execute("SELECT studentID FROM attendance WHERE attendDate = '" + self.date + "' and present = '1' and groupsetID = '" + self.set[1] + "'")
        self.attendees = self.c.fetchall()
        self.c.execute("SELECT studentID FROM attendance WHERE attendDate = '" + self.date + "' and present = '0' and groupsetID = '" + self.set[1] + "'")
        self.absentees = self.c.fetchall()
        self.displaylabels22()

    # Produces a label for each student with their present or absent status for the selected date
    def displaylabels22(self):
        self.bottomFrame.pack_forget()
        self.bottomFrame = Frame(self.mainFrame, bg="snow")
        self.bottomFrame.pack(fill=X, expand=1, side=BOTTOM, anchor=N)
        c = 1
        for i in self.attendees:
            student = Student()
            student.setID(i[0])
            self.c.execute("SELECT studentName FROM student WHERE studentID = '" + i[0] + "'")
            studentName = self.c.fetchone()[0]
            self.c.execute("SELECT studentSurname FROM student WHERE studentID = '" + i[0] + "'")
            studentSurname = self.c.fetchone()[0]

            tName = Label(self.bottomFrame, text="Student Name", bg="grey52")
            tSet = Label(self.bottomFrame, text="Set", bg="grey52")
            tPresent = Label(self.bottomFrame, text="Present/Absent", bg="grey52")

            tName.grid(row=0, column=0, sticky=N)
            tSet.grid(row=0, column=1, sticky=N)
            tPresent.grid(row=0, column=2, sticky=N)

            self.sName = Label(self.bottomFrame, text=studentName + " " + studentSurname, bg="snow", width=20)
            self.sSet = Label(self.bottomFrame, text=self.set[1], bg="snow", width=10)
            self.sPresent = Label(self.bottomFrame, text="Present", bg="forest green", width=13)

            self.sName.grid(row=c, column=0)
            self.sSet.grid(row=c, column=1)
            self.sPresent.grid(row=c, column=2)
            c += 1
        d = 1
        for i in self.absentees:
            student = Student()
            student.setID(i[0])
            self.c.execute("SELECT studentName FROM student WHERE studentID = '" + i[0] + "'")
            studentName = self.c.fetchone()[0]
            self.c.execute("SELECT studentSurname FROM student WHERE studentID = '" + i[0] + "'")
            studentSurname = self.c.fetchone()[0]

            tName = Label(self.bottomFrame, text="Student Name", bg="grey52", width=20)
            tSet = Label(self.bottomFrame, text="Set", bg="grey52", width=10)
            tPresent = Label(self.bottomFrame, text="Present/Absent", bg="grey52", width=13)

            tName.grid(row=0, column=0, sticky=N)
            tSet.grid(row=0, column=1, sticky=N)
            tPresent.grid(row=0, column=2, sticky=N)

            self.sName = Label(self.bottomFrame, text=studentName + " " + studentSurname, bg="snow", width=20)
            self.sSet = Label(self.bottomFrame, text=self.set[1], bg="snow", width=10)
            self.sPresent = Label(self.bottomFrame, text="Absent", bg="firebrick1", width=13)

            self.sName.grid(row=c + d, column=0)
            self.sSet.grid(row=c + d, column=1)
            self.sPresent.grid(row=c + d, column=2)
            d += 1




