from tkinter import *
from studentViewUI import *

# Displays a main window and a menu for different views


class MainWindow(object):

    def __init__(self):

        # Plan here is to have the login return the ID
        # Test IDs st147707702 17153811308 17151025709 17145725904
        self.setID("st147707702")

        # For Teachers
        if self.userID[0:2] == "st":
            self.root = Tk()

            # Creates frames within the main window on the left and right
            # Left frame is for the menu, right for the display
            self.menuFrame = Frame()
            self.menuFrame.pack(fill=Y, side=LEFT)
            self.displayFrame = Frame()
            self.displayFrame.pack(fill=BOTH, expand=1, side=RIGHT)

            # Creates another frame within the display frame. This allows
            # it to be displayed and hidden separately from everything else
            self.createmainframe()

            # Adds menu buttons
            viewGrades = Button(self.menuFrame, text="View grades", command=self.displaygrades)
            viewGrades.pack()
            upGrades = Button(self.menuFrame, text="Update Grades", command=self.updategrades)
            upGrades.pack()
            logOut = Button(self.menuFrame, text="Log out", command=self.root.quit)
            logOut.pack()

            self.root.mainloop()

        # For students
        if self.userID[0:1].isnumeric():

            self.root = Tk()

            self.menuFrame = Frame()
            self.menuFrame.pack(fill=Y, side=LEFT)
            self.displayFrame = Frame()
            self.displayFrame.pack(fill=BOTH, expand=1, side=RIGHT)

            self.createmainframe()

            student = Button(self.menuFrame, text="View my grades", command=self.studentview)
            student.pack()
            logOut = Button(self.menuFrame, text="Log out", command=self.root.quit)
            logOut.pack()

            self.root.mainloop()

    def createmainframe(self):
        self.mainFrame = Frame(self.displayFrame)
        self.mainFrame.pack(side=RIGHT, fill=BOTH, expand=1)

    def resetframe(self):
        # 'Forgets' the display frame and creates a new empty one
        self.mainFrame.pack_forget()
        self.mainFrame = Frame(self.displayFrame)
        self.mainFrame.pack(side=RIGHT, fill=BOTH, expand=1)

    def setID(self, userID):
        self.userID = userID

    def studentview(self):
        self.resetframe()
        student = Student()
        student.setID(self.userID)
        student.getinfo()
        displaystudentview(student, self.mainFrame)
        self.root.title(student.userName + " " + student.userSurname)

    def displaygrades(self):
        self.resetframe()
        label = Label(self.mainFrame, text="VIEW GRADES", bg="red")
        label.pack(fill=BOTH)
        self.root.title("Viewing student grades")

    def updategrades(self):
        self.resetframe()
        label = Label(self.mainFrame, text="UPDATE GRADES", bg="green")
        label.pack(fill=BOTH)
        self.root.title("Updating student grades")

mainWindow = MainWindow()
