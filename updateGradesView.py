
from tkinter import *
from tkinter import ttk
import sqlite3
import time

#print(grades)
# returns
# [(6, 'a', '2017', 1, 'M03011', 'st81623', 7, 0, 'A', '1734881', 6)
# groupsetID, groupsetName, year, semester, moduleCode, teacherID, (grade)id, grade, gradeType, studentID, groupsetID


##########################################################################
# dataGrid class
#dataGrid = updateGradesClass("st81623", "mainCanvas")

class updateGradesClass():

    def __init__(self, teacherID, master):
        # variables
        # fieldsToShow = [1,2,3,4,8,9]
        self.fieldsToShow = [None, "groupsetName", "year", "semester", "moduleCode", None, None, "grade", "gradeType",
                        "studentID", None]
        # fieldToEdit = [7]
        self.fieldToEdit = 7

        self.conn = sqlite3.connect("db/crDBv2W10Demo.db")
        self.cursor = self.conn.cursor()
        self.grades = None

        self.master = master
        self.teacherID = teacherID

        self.dbFetch()
        self.moduleIDs = []
        for item in self.grades:
            setPerMtxt = str(item[4]) + " / " + str(item[1])
            if setPerMtxt not in self.moduleIDs:
                self.moduleIDs.append(setPerMtxt)
        self.actModule = self.retrieveModuleID( self.moduleIDs[0] )
        self.col = len(self.grades[0])
        self.row = len(self.grades)
        self.grid = [[0] * (self.col+1)] * (self.row + 1) # +1 because of header

        ########### create widgets
        # main frame, placeholder for the data grid
        self.mainFrame = Frame(self.master)
        self.mainFrame.pack(side=LEFT, fill=BOTH, expand=True)

        #############################################
        # add topFrame to mainFrame
        # frame with module select, ?set select?, module info, etc.
        self.topFrame = Frame(self.mainFrame)
        self.topFrame.config(height=200, relief=RAISED, borderwidth=1, padx=10, pady=15)
        self.topFrame.pack(side=TOP, fill=X, expand=False)

        # add drop down list to frame
        # get all modules related to teacherID in to an array
        # on select refresh (update()) frame
        self.modCombobox = ttk.Combobox(self.topFrame, textvariable=self.moduleIDs)
        self.modCombobox["values"] = self.moduleIDs
        self.modCombobox.bind("<<ComboboxSelected>>", self.recreateFrame)
        self.modCombobox.pack(side=LEFT)

        # add canvas to mainFrame
        # to sort out scroll for data grid
        self.mainCanvas = Canvas(self.mainFrame)
        self.mainCanvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.gridFrame = Frame(self.mainCanvas)
        #self.gridFrame.pack(side=LEFT, fill=BOTH, expand=True)

        # add scrollbar to mainFrame
        self.vScrbar = Scrollbar(self.mainFrame, orient=VERTICAL)
        self.vScrbar.pack(side=RIGHT, fill=Y)
        self.hScrbar = Scrollbar(self.mainFrame, orient=HORIZONTAL)
        self.hScrbar.pack(side=BOTTOM, fill=X)

        #############################################
        self.dataGrid()

        # link scrollbar to canvas
        self.vScrbar.config(command=self.mainCanvas.yview)
        self.hScrbar.config(command=self.mainCanvas.xview)

    def setActModule(self, actMod):
        self.actModule = actMod

    def retrieveModuleID(self, setPerModule):
        return setPerModule[0:6]

    def retrieveModuleInfo(self):
        theModule = [self.actModule]
        self.cursor.execute("SELECT * FROM module WHERE moduleID=?", theModule)
        fetchData = self.cursor.fetchone()
        # not quite finished


    def dbFetch(self):
        #stID = "st81623"
        thisYear = str(time.strftime("%Y"))  # 4 digit year
        bondQ = [self.teacherID, thisYear]
        self.cursor.execute("SELECT * FROM groupset INNER JOIN grade ON groupset.groupsetID=grade.groupsetID "
                       "WHERE groupset.teacherID=? AND groupset.year=? ORDER BY groupsetID", bondQ)
        self.grades = self.cursor.fetchall()

    ###################################################################
    # datagrid itself

    def dataGrid(self):
        # create frame to encapsulate
        self.gridFrame = Frame(self.mainCanvas)
        self.gridFrame.pack(side=LEFT, fill=BOTH, expand=True)
        setPerModule = self.modCombobox.get()
        if setPerModule == "":
            set = self.moduleIDs[0][-5:]
        else :
            set = setPerModule[-5:]
        # print( set )

        for r in range(0, self.row):
            # set background color variable
            if r % 2 != 0:
                bckg = "gray90"
            else:
                bckg = "gray70"

            # fill up grid with widgets
            for c in range(0, self.col):
                #print(str(self.col) +" : "+ str(abs(1-self.col)))
                if self.actModule == "" or self.actModule == self.grades[r][4] and set == self.grades[r][1]:
                    if c == 0:
                        self.grid[r][c] = Label(self.gridFrame, text=r, relief=FLAT, bg=bckg)
                        # add widget to grid at end
                        self.grid[r][c].grid(row=r+1, column=c, ipadx=10, ipady=5, sticky=NSEW)
                    elif self.fieldsToShow[c] is not None:
                        if c == self.fieldToEdit:
                            txt = self.grades[r][c]
                            self.grid[r][c] = Entry(self.gridFrame, width=3, relief=FLAT, bg="white")
                            # bind return key to entry to do update 1-by-1
                            self.grid[r][c].bind('<Return>', lambda event, gradeID=self.grades[r][6] : self.updateGrade(event.widget.get(),gradeID) )
                            self.grid[r][c].insert(END, txt)
                        else:
                            txt = self.grades[r][c]
                            self.grid[r][c] = Label(self.gridFrame, text=txt, relief=FLAT, bg=bckg)
                        # add widget to grid at end
                        self.grid[r][c].grid(row=r+1, column=c, ipadx=10, ipady=5, sticky=NSEW)

        # add frame to canvas to make it scrollable
        self.mainCanvas.create_window(0, 0, window=self.gridFrame, anchor=NW)

        # set scroll region to actual frame size
        self.gridFrame.update()
        gridHeight = 20 + self.gridFrame.winfo_height()
        gridWidth = self.gridFrame.winfo_width()
        self.mainCanvas.config(yscrollcommand=self.vScrbar.set, xscrollcommand=self.hScrbar.set)
        self.mainCanvas.config(scrollregion=(0, 0, gridWidth, gridHeight))

    #redraw the frame after modify
    def recreateFrame(self, event):
        actMod = self.retrieveModuleID( self.modCombobox.get() )
        self.setActModule( actMod )
        # print( actMod  )
        self.gridFrame.destroy()
        self.dbFetch()
        self.dataGrid()
        self.mainCanvas.update()

    # binding test
    def doGet(self, event):
        print(event.widget.get())

    # update grade in DB
    def updateGrade(self, newGrade, gradeID):
        # body for batch update from top frame button

        self.cursor.execute("SELECT grade FROM grade WHERE id=?", [gradeID])
        print("UPDATE start >> new grade: " + str(newGrade) +", where grade ID: "+ str(gradeID))
        pushData = (int(newGrade), int(gradeID))
        print(pushData)
        self.cursor.execute("UPDATE grade SET grade=? WHERE id=?", pushData)
        self.recreateFrame(1)
        self.cursor.execute("SELECT grade FROM grade WHERE id=?", [gradeID])
        feedback = self.cursor.fetchone()
        print("grade value after: ")
        print(feedback)
        self.conn.commit()

#########################################################

# if __name__ == '__main__':
#     root = Tk()
#     root.update()
#
#     #########################################################
#     # instantiate class
#     # the actual data grid
#     # teachers with more than one set: st82277, st81623
#     # dataGrid = updateGradesClass("st81623", mainCanvas)
#
#     dataGrid = updateGradesClass("st81623", root)
#
#     root.geometry("800x600")
#     root.mainloop()
