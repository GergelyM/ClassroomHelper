from tkinter import *
from loginHandler import LoginHandler
from dbHandler import *

# Currently uses loginhandler.py to verify a login and displays the grades for that students module.
# Only displays a single module right now, very unfinished.
# Sorry it's messy - Connor

# Test IDs  17153811308
#           17151025709
#           17145725904
# Others do not work as no teacher for M03010
# Remember to comment out lines 88 and 89 of loginhandler.py or login twice.

class Student(object):
    crDB = DbConn("db/crDB.db")
    c = crDB.cursor

    def __init__(self):
        user = LoginHandler()
        self.userID = user.login()
        self.c.execute("SELECT studentName FROM student WHERE studentID = '" + self.userID + "'")
        self.userName = self.c.fetchone()[0]
        self.c.execute("SELECT studentSurname FROM student WHERE studentID = '" + self.userID + "'")
        self.userSurname = self.c.fetchone()[0]
        self.userModuleCode = []
        self.c.execute("SELECT moduleCode FROM grade WHERE studentID = '" + self.userID + "'")
        self.userModuleCode = self.c.fetchone()[0]
        self.userModuleNames = []
        self.c.execute("SELECT moduleName FROM module WHERE moduleCode = '" + self.userModuleCode + "'")
        self.userModuleNames = self.c.fetchone()[0]
        self.userGrade = []
        self.c.execute("SELECT grade FROM grade WHERE studentID = '" + self.userID + "'")
        self.userGrade = self.c.fetchone()[0]
        self.userYear = []
        self.c.execute("SELECT year FROM grade WHERE studentID = '" + self.userID + "'")
        self.userYear = self.c.fetchone()[0]
        self.userSemester = []
        self.c.execute("SELECT semester FROM grade WHERE studentID = '" + self.userID + "'")
        self.userSemester = self.c.fetchone()[0]
        self.userTeacherID = []
        self.c.execute("SELECT teacherID FROM teachedby WHERE moduleCode = '" + self.userModuleCode + "'")
        self.userTeacherID = self.c.fetchone()[0]
        self.userTeacherName = []
        self.c.execute("SELECT teacherName FROM teacher WHERE teacherID = '" + self.userTeacherID + "'")
        self.userTeacherName = self.c.fetchone()[0]
        self.userTeacherSurname = []
        self.c.execute("SELECT teacherSurname FROM teacher WHERE teacherID = '" + self.userTeacherID + "'")
        self.userTeacherSurname = self.c.fetchone()[0]

student = Student()

root = Tk()


#        Headers
intro = Label(root, text="Viewing grades for ", bg="chartreuse3")
sName = Label(root, text=student.userName + " " + student.userSurname, bg="chartreuse3")
sID = Label(root, text=student.userID, bg="chartreuse3")

intro.grid(row=0, column=0, sticky=W + E)
sName.grid(row=0, column=1, sticky=W + E)
sID.grid(row=0, column=2, sticky=W + E)

#       Column Titles
mName = Label(root, text="Module Name", bg="grey52")
mCode = Label(root, text="Module Code", bg="grey52")
mGrade = Label(root, text="Grade", bg="grey52")
mYear = Label(root, text="Year", bg="grey52")
mSemester = Label(root, text="Semester", bg="grey52")
mTeacher = Label(root, text="Teacher", bg="grey52")

mName.grid(row=2, column=0, sticky=W+E)
mCode.grid(row=2, column=1, sticky=W+E)
mGrade.grid(row=2, column=2, sticky=W+E)
mYear.grid(row=2, column=3, sticky=W+E)
mSemester.grid(row=2, column=4, sticky=W+E)
mTeacher.grid(row=2, column=5, sticky=W+E)

#      Aesthetics
alabel = Label(root, text=" ", bg="chartreuse3")
alabel.grid(row=1, columnspan=6, sticky=W+E)

alabel2 = Label(root, text=" ", bg="chartreuse3")
alabel2.grid(row=0, column=3, columnspan=3, sticky=W+E)


#      Columns of Data
uP = Label(root, text=student.userModuleNames, bg="snow") # module name
uPCode = Label(root, text=student.userModuleCode, bg="snow") # moduleCode
uPGrade = Label(root, text=student.userGrade, bg="snow") # Grade
uPyear = Label(root, text=student.userYear, bg="snow") # Year
uPSemester = Label(root, text=student.userSemester, bg="snow") # Semester
uPTeacher = Label(root, text=student.userTeacherName + " " + student.userTeacherSurname, bg="snow") # Teacher

uP.grid(row=3, column=0, sticky=W + E)
uPCode.grid(row=3, column=1, sticky=W + E)
uPGrade.grid(row=3, column=2, sticky=W + E)
uPyear.grid(row=3, column=3, sticky=W + E)
uPSemester.grid(row=3, column=4, sticky=W + E)
uPTeacher.grid(row=3, column=5, sticky=W + E)



root.mainloop()