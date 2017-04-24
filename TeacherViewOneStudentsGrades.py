from tkinter import *
from dbHandler import *
from studentViewUI import *

# Teacher object used for storing info about a teachers tought modules and students
class Teacher(object):

    crDB = DbConn("db/crDBv2.db")
    c = crDB.cursor


    def __init__(self):
        self.userID = ""
        self.userName = ""
        self.userSurname = ""
        self.sets = []
        self.studentIDs = []
        self.studentSurnames = []
        self.studentNames = []
        self.userModuleCode = []
        self.userModuleNames = []
        self.studentcompletenames = []

    def setID(self, userID):
        self.userID = userID

    # Finds all the modules the teacher teaches and all the students attending that module
    def getInfo(self):
        self.c.execute("SELECT teacherName FROM teacher WHERE teacherID = '" + self.userID + "'")
        self.userName = self.c.fetchone()[0]
        self.c.execute("SELECT teacherSurname FROM teacher WHERE teacherID = '" + self.userID + "'")
        self.userSurname = self.c.fetchone()[0]
        self.c.execute("SELECT groupsetID FROM groupset WHERE teacherID = '" + self.userID + "'")
        self.sets = self.c.fetchall()

        c = 0
        for i in self.sets:
            self.c.execute("SELECT moduleCode FROM groupset WHERE groupsetID = '" + str(i[0]) + "'")
            self.userModuleCode.append(self.c.fetchone())
            self.c.execute("SELECT moduleName FROM module WHERE moduleCode = '" + self.userModuleCode[c][0] + "'")
            self.userModuleNames.append(self.c.fetchone())
            self.c.execute("SELECT studentID FROM grade WHERE groupsetID = '" + str(i[0]) + "'")
            self.studentIDs.append(self.c.fetchall())
            c += 1
        d = 0
        for j in self.studentIDs:
            for l in j:
                self.c.execute("SELECT studentName FROM student WHERE studentID = '" + str(l[0]) + "'")
                self.studentNames.append(self.c.fetchone())
                self.c.execute("SELECT studentSurname FROM student WHERE studentID = '" + str(l[0]) + "'")
                self.studentSurnames.append(self.c.fetchone())
            d += 1

        e = 0
        for k in self.studentNames:
            self.studentcompletenames.append(self.studentNames[e][0] + " " + self.studentSurnames[e][0])
            e += 1

# Creates a window that is placed in the display frame, has a top frame for drop down menus and a bottom frame for the
# grades
class Display(object):


    crDB = DbConn("db/crDB.db")
    c = crDB.cursor

    def __init__(self, teacher, mainFrame):
        self.mainFrame = mainFrame
        self.teacher = teacher
        self.topFrame = Frame(self.mainFrame, bg="chartreuse3")
        self.topFrame.pack(fill=BOTH, expand=1, side=TOP)
        self.bottomFrame = Frame(self.mainFrame, bg="snow")
        self.bottomFrame.pack(fill=BOTH, expand=1, side=BOTTOM)

        # Creates a drop down menu that allows the teacher to select one of the students they teach
        self.grade = []
        self.teacher.studentcompletenames = list(set(self.teacher.studentcompletenames))
        self.var = StringVar(self.topFrame)
        self.var.set("Select Student")
        self.menu = OptionMenu(self.topFrame, self.var, *self.teacher.studentcompletenames)
        self.menu.pack(side="left")
        self.search = Button(self.topFrame, text="Search", command=self.search2, relief=GROOVE)
        self.search.pack(side="left", padx=10, pady=10)

    # creates a student object of the selected student and fetches all their grade info
    def search2(self):
        self.studentname = self.var.get()
        self.names = self.studentname.split()
        self.c.execute("SELECT studentID FROM student WHERE studentName = '" + self.names[0] + "'")
        self.studentID = self.c.fetchone()[0]
        self.student = Student()
        self.student.setID(self.studentID)
        self.student.getinfoforteacher(self.teacher)


        # Headers for the grade columns
        self.mName = Label(self.bottomFrame, text="Module Name", bg="grey52")
        self.mCode = Label(self.bottomFrame, text="Module Code", bg="grey52")
        self.mGradeType = Label(self.bottomFrame, text="Grade Type", bg="grey52")
        self.mGrade = Label(self.bottomFrame, text="Grade", bg="grey52")
        self.mYear = Label(self.bottomFrame, text="Year", bg="grey52")
        self.mSemester = Label(self.bottomFrame, text="Semester", bg="grey52")
        self.mTeacher = Label(self.bottomFrame, text="Teacher", bg="grey52")

        self.mName.grid(row=2, column=0, sticky=W + E)
        self.mCode.grid(row=2, column=1, sticky=W + E)
        self.mGradeType.grid(row=2, column=2, sticky=W + E)
        self.mGrade.grid(row=2, column=3, sticky=W + E)
        self.mYear.grid(row=2, column=4, sticky=W + E)
        self.mSemester.grid(row=2, column=5, sticky=W + E)
        self.mTeacher.grid(row=2, column=6, sticky=W + E)

        for i in self.teacher.sets:
            self.c.execute("SELECT gradeType FROM grade WHERE studentID = '" + self.studentID + "' and groupsetID = '" + str(i[0]) + "'" )
            self.grade.append(self.c.fetchall())

        self.displayLabels()

    # Produces a label for each grade
    def displayLabels(self):

        c = 0
        for i in self.student.userModuleCode:
            uP = Label(self.bottomFrame, text=self.student.userModuleNames[c][0], bg="snow")  # module name
            uPCode = Label(self.bottomFrame, text=self.student.userModuleCode[c][0], bg="snow")  # moduleCode
            uPGradeType = Label(self.bottomFrame, text="Assignment", bg="snow")  # GradeType
            if self.student.gradeAssignment[c][0][0] >= 70:
                uPGrade = Label(self.bottomFrame, text=self.student.gradeAssignment[c][0], bg="green3")  # Grade
            elif self.student.gradeAssignment[c][0][0] >= 60:
                uPGrade = Label(self.bottomFrame, text=self.student.gradeAssignment[c][0], bg="OliveDrab1")
            elif self.student.gradeAssignment[c][0][0] >= 50:
                uPGrade = Label(self.bottomFrame, text=self.student.gradeAssignment[c][0], bg="yellow2")
            elif self.student.gradeAssignment[c][0][0] >= 40:
                uPGrade = Label(self.bottomFrame, text=self.student.gradeAssignment[c][0], bg="orange2")
            elif self.student.gradeAssignment[c][0][0] < 40:
                uPGrade = Label(self.bottomFrame, text=self.student.gradeAssignment[c][0], bg="firebrick1")
            uPyear = Label(self.bottomFrame, text=self.student.userYear[c][0], bg="snow")  # Year
            uPSemester = Label(self.bottomFrame, text=self.student.userSemester[c][0], bg="snow")  # Semester
            uPTeacher = Label(self.bottomFrame, text=self.student.userTeacherName[c][0] + " " + self.student.userTeacherSurname[c][0],
                              bg="snow")  # Teacher

            uP.grid(row=3 + c, column=0, sticky=W + E)
            uPCode.grid(row=3 + c, column=1, sticky=W + E)
            uPGradeType.grid(row=3 + c, column=2, sticky=W + E)
            uPGrade.grid(row=3 + c, column=3, sticky=W + E)
            uPyear.grid(row=3 + c, column=4, sticky=W + E)
            uPSemester.grid(row=3 + c, column=5, sticky=W + E)
            uPTeacher.grid(row=3 + c, column=6, sticky=W + E)

            c += 1

        d = 0
        for i in self.student.userModuleCode:
            uP = Label(self.bottomFrame, text=self.student.userModuleNames[d][0], bg="snow")  # module name
            uPCode = Label(self.bottomFrame, text=self.student.userModuleCode[d][0], bg="snow")  # moduleCode
            uPGradeType = Label(self.bottomFrame, text="Exam", bg="snow")  # GradeType
            if self.student.gradeExam[d][0][0] >= 70:
                uPGrade = Label(self.bottomFrame, text=self.student.gradeExam[d][0], bg="green3")
            elif self.student.gradeExam[d][0][0] >= 60:
                uPGrade = Label(self.bottomFrame, text=self.student.gradeExam[d][0], bg="OliveDrab1")
            elif self.student.gradeExam[d][0][0] >= 50:
                uPGrade = Label(self.bottomFrame, text=self.student.gradeExam[d][0], bg="yellow2")
            elif self.student.gradeExam[d][0][0] >= 40:
                uPGrade = Label(self.bottomFrame, text=self.student.gradeExam[d][0], bg="orange2")
            elif self.student.gradeExam[d][0][0] < 40:
                uPGrade = Label(self.bottomFrame, text=self.student.gradeExam[d][0], bg="firebrick1")
            uPyear = Label(self.bottomFrame, text=self.student.userYear[d][0], bg="snow")  # Year
            uPSemester = Label(self.bottomFrame, text=self.student.userSemester[d][0], bg="snow")  # Semester
            uPTeacher = Label(self.bottomFrame, text=self.student.userTeacherName[d][0] + " " + self.student.userTeacherSurname[d][0],
                              bg="snow")  # Teacher

            uP.grid(row=3 + c, column=0, sticky=W + E)
            uPCode.grid(row=3 + c, column=1, sticky=W + E)
            uPGradeType.grid(row=3 + c, column=2, sticky=W + E)
            uPGrade.grid(row=3 + c, column=3, sticky=W + E)
            uPyear.grid(row=3 + c, column=4, sticky=W + E)
            uPSemester.grid(row=3 + c, column=5, sticky=W + E)
            uPTeacher.grid(row=3 + c, column=6, sticky=W + E)

            c += 1
            d += 1

        e = 0
        for i in self.student.userModuleCode:
            uP = Label(self.bottomFrame, text=self.student.userModuleNames[e][0], bg="snow")  # module name
            uPCode = Label(self.bottomFrame, text=self.student.userModuleCode[e][0], bg="snow")  # moduleCode
            uPGradeType = Label(self.bottomFrame, text="Attendance", bg="snow")  # GradeType
            if self.student.gradeAttendance[e][0][0] >= 70:
                uPGrade = Label(self.bottomFrame, text=self.student.gradeAttendance[e][0], bg="green3")
            elif self.student.gradeAttendance[e][0][0] >= 60:
                uPGrade = Label(self.bottomFrame, text=self.student.gradeAttendance[e][0], bg="OliveDrab1")
            elif self.student.gradeAttendance[e][0][0] >= 50:
                uPGrade = Label(self.bottomFrame, text=self.student.gradeAttendance[e][0], bg="yellow2")
            elif self.student.gradeAttendance[e][0][0] >= 40:
                uPGrade = Label(self.bottomFrame, text=self.student.gradeAttendance[e][0], bg="orange2")
            elif self.student.gradeAttendance[e][0][0] < 40:
                uPGrade = Label(self.bottomFrame, text=self.student.gradeAttendance[e][0], bg="firebrick1")
            uPyear = Label(self.bottomFrame, text=self.student.userYear[e][0], bg="snow")  # Year
            uPSemester = Label(self.bottomFrame, text=self.student.userSemester[e][0], bg="snow")  # Semester
            uPTeacher = Label(self.bottomFrame, text=self.student.userTeacherName[e][0] + " " + self.student.userTeacherSurname[e][0],
                              bg="snow")  # Teacher

            uP.grid(row=3 + c, column=0, sticky=W + E)
            uPCode.grid(row=3 + c, column=1, sticky=W + E)
            uPGradeType.grid(row=3 + c, column=2, sticky=W + E)
            uPGrade.grid(row=3 + c, column=3, sticky=W + E)
            uPyear.grid(row=3 + c, column=4, sticky=W + E)
            uPSemester.grid(row=3 + c, column=5, sticky=W + E)
            uPTeacher.grid(row=3 + c, column=6, sticky=W + E)

            c += 1
            e += 1






