from tkinter import *
from studentViewUI import *
from TeacherViewOneStudentsGrades import *
from ViewAttendance import *

# Displays a main window and a menu for different views


class MainWindow(object):

    crDB = DbConn("db/crDBv2.db")
    c = crDB.cursor

    def __init__(self):

        # Plan here is to have the login return the ID
        # Test IDs st82277 1733675 1734658 1734584
        self.setID("st82277")
        self.userName = ""
        self.userSurname = ""

        # For Teachers
        if self.userID[0:2] == "st":
            self.root = Tk()
            self.root.geometry("%dx%d+%d+%d" % (800, 600, 100, 20))

            # Creates frames within the main window on the left and right
            # Left frame is for the menu, right for the display
            self.menuFrame = Frame(bg="chartreuse3")
            self.menuFrame.pack(fill=Y, side=LEFT)
            self.displayFrame = Frame(bg="snow")
            self.displayFrame.pack(fill=BOTH, expand=1, side=RIGHT, anchor=N)





            # Creates another frame within the display frame. This allows
            # it to be displayed and hidden separately from everything else
            self.createmainframe()

            # Creates welcome label displaying teacher name
            self.c.execute("SELECT teacherName FROM teacher WHERE teacherID = '" + self.userID + "'")
            self.userName = self.c.fetchone()[0]
            self.c.execute("SELECT teacherSurname FROM teacher WHERE teacherID = '" + self.userID + "'")
            self.userSurname = self.c.fetchone()[0]

            welcome = Label(self.mainFrame, text="Welcome " + self.userName + " " +  self.userSurname, bg="snow")
            welcome.pack()

            # Adds menu buttons
            viewGrades = Button(self.menuFrame, text="View grades for set", command=self.displaygrades, width=22, relief=GROOVE)
            viewGrades.pack()
            upGrades = Button(self.menuFrame, text="Update Grades", command=self.updategrades, width=22, relief=GROOVE)
            upGrades.pack()
            viewGradesOneStudent = Button(self.menuFrame, text="View grades for one student", command=self.viewonestudentsgrades, width=22, relief=GROOVE)
            viewGradesOneStudent.pack()
            viewAttendance = Button(self.menuFrame, text="View attendance", command=self.viewattendance, width=22, relief=GROOVE)
            viewAttendance.pack()

            logOut = Button(self.menuFrame, text="Log out", command=self.root.quit, width=22, relief=GROOVE)
            logOut.pack()

            self.root.mainloop()

        # For students
        if self.userID[0:1].isnumeric():

            self.root = Tk()
            self.root.geometry("%dx%d+%d+%d" % (800, 600, 100, 20))

            self.menuFrame = Frame(bg="chartreuse3")
            self.menuFrame.pack(fill=Y, side=LEFT)
            self.displayFrame = Frame(bg="snow")
            self.displayFrame.pack(fill=BOTH, expand=1, side=RIGHT, anchor=N)

            self.createmainframe()

            # Creates welcome label displaying student name
            self.c.execute("SELECT studentName FROM student WHERE studentID = '" + self.userID + "'")
            self.userName = self.c.fetchone()[0]
            self.c.execute("SELECT studentSurname FROM student WHERE studentID = '" + self.userID + "'")
            self.userSurname = self.c.fetchone()[0]

            welcome = Label(self.mainFrame, text="Welcome " + self.userName + " " + self.userSurname, bg="snow")
            welcome.pack()

            student = Button(self.menuFrame, text="View my grades", command=self.studentview, width=22, relief=GROOVE)
            student.pack()
            logOut = Button(self.menuFrame, text="Log out", command=self.root.quit, width=22, relief=GROOVE)
            logOut.pack()

            self.root.mainloop()

    def createmainframe(self):
        self.mainFrame = Frame(self.displayFrame, bg="snow")
        self.mainFrame.pack(side=RIGHT, fill=BOTH, expand=1)

    def resetframe(self):
        # 'Forgets' the display frame and creates a new empty one
        self.mainFrame.pack_forget()
        self.mainFrame = Frame(self.displayFrame, bg="snow")
        self.mainFrame.pack(side=RIGHT, fill=X, expand=1, anchor=N)

    def setID(self, userID):
        self.userID = userID

    def studentview(self):
        self.resetframe()
        student = Student()
        student.setID(self.userID)
        student.getinfo()
        displaystudentview(student, self.mainFrame)
        displayLabels(student, self.mainFrame)
        self.root.title(student.userName + " " + student.userSurname)
        self.root.title("Viewing your grades")

    def viewonestudentsgrades(self):
        self.resetframe()
        teacher = Teacher()
        teacher.setID(self.userID)
        teacher.getInfo()
        windo = Display(teacher, self.mainFrame)
        self.root.title("Viewing grades for one student")

    def viewattendance(self):
        self.resetframe()
        teacher = Teacher()
        teacher.setID(self.userID)
        teacher.getInfo()
        windoo = Window(teacher, self.mainFrame)
        windoo.displayonestudentview()
        self.root.title("Viewing Attendance")

    def displaygrades(self):
        self.resetframe()
        label = Label(self.mainFrame, text="VIEW GRADES FOR SET PLACEHOLDER", bg="red")
        label.pack(fill=BOTH)
        self.root.title("Viewing grades for one set")

    def updategrades(self):
        self.resetframe()
        label = Label(self.mainFrame, text="UPDATE GRADES PLACEHOLDER", bg="green")
        label.pack(fill=BOTH)
        self.root.title("Updating student grades")

mainWindow = MainWindow()
