import sqlite3
from tkinter import *
from tkinter import ttk
import dbHandler
import time

#print(grades)
# returns
# [(6, 'a', '2017', 1, 'M03011', 'st81623', 7, 0, 'A', '1734881', 6)
# groupsetID, groupsetName, year, semester, moduleCode, teacherID, (grade)id, grade, gradeType, studentID, groupsetID

#fieldsToShow = [1,2,3,4,8,9]
fieldsToShow = [None,"groupsetName","year","semester","moduleCode",None,None,"grade","gradeType","studentID",None]
#fieldToEdit = [7]
fieldToEdit = 7

##########################################################################
# field class for dataGrid

class field():
    #vars
    typ = None
    master = ""
    posRow = 0
    posCol = 0
    defText = ""
    width = 0
    # relief based on type
    relief = FLAT #FLAT, RAISED, SUNKEN, GROOVE, RIDGE

    def __init__(self, type, master, posR, posC, defTxt, wid):
        self.master = master
        self.posRow = posR
        self.posCol = posC
        self.defText = defTxt
        self.width = wid
        #types: label, entry, header
        if type == "header":
            print("header")
            #call header
        elif type == "entry":
            print("entry")
            #call entry
        else:
            print("label")
            #call label

    #methods
    #def insertHeader(self):



##########################################################################
# dataGrid class
#dataGrid = updateGradesClass("st81623", "mainCanvas")

class updateGradesClass():
    #variables
    conn = dbHandler.DbConn("db/crDBv2.db")
    cursor = conn.cursor
    grades = None
    # [[element] * numcols] * numrows
    #actModule = ""

    def __init__(self, teacherID, master):
        self.master = master
        self.gridFrame = Frame(self.master)
        self.teacherID = teacherID
        self.dbFetch()
        #print(self.grades)
        self.moduleIDs = []
        for item in self.grades:
            if item[4] not in self.moduleIDs:
                self.moduleIDs.append(item[4])
        self.actModule = self.moduleIDs[0]
        #print(self.moduleIDs)
        #print(self.actModule)
        self.col = len(self.grades[0])
        self.row = len(self.grades)
        self.grid = [[0] * (self.col+1)] * (self.row + 1) # +1 because of header

    def setActModule(self, actMod):
        self.actModule = actMod

    def dbFetch(self):
        #tID = "st81623"
        thisYear = str(time.strftime("%Y"))  # 4 digit year
        bondQ = [self.teacherID, thisYear]
        self.cursor.execute("SELECT * FROM groupset INNER JOIN grade ON groupset.groupsetID=grade.groupsetID "
                       "WHERE groupset.teacherID=? AND groupset.year=? ORDER BY groupsetID", bondQ)
        self.grades = self.cursor.fetchall()
        #return grades

        # print(grades)
        # returns
        # [(6, 'a', '2017', 1, 'M03011', 'st81623', 7, 0, 'A', '1734881', 6)
        # groupsetID, groupsetName, year, semester, moduleCode, teacherID, (grade)id, grade, gradeType, studentID, groupsetID

    ###################################################################
    # todo-Gary limit the data displayed
    # add update button to each line
    # create db update function
    #   collect data for SQL update
    #   execute SQL
    #   commit DB if needed
    ###################################################################

    def dataGrid(self):
        # create frame to encapsulate
        self.gridFrame = Frame(self.master)
        self.gridFrame.pack(side=LEFT, fill=BOTH, expand=True)
        self.actModule = modCombobox.get()

        for r in range(0, self.row):
            #add header fields to row 0
            # if r == 0:
            #     headerFields = []
            #     i = 0
            #     while i < len(fieldsToShow):
            #         #headerFields.append()
            #         headerFields[i].config(relief=RAISED)
            #         headerFields[i].grid(row=0, column=i, ipadx=10, ipady=5, sticky=W)
            #         #headerFields[i].pack(side=LEFT)
            #         i += 1
            for c in range(0, self.col):
                #print(str(self.col) +" : "+ str(abs(1-self.col)))
                if self.actModule == "" or self.actModule == self.grades[r][4]:
                    if c == 0:
                        self.grid[r][c] = Label(self.gridFrame, text=r)
                    elif fieldsToShow[c] is not None:
                        if c == fieldToEdit:
                            txt = self.grades[r][c]
                            self.grid[r][c] = Entry(self.gridFrame, width=5)
                            self.grid[r][c].insert(0, txt)
                        else:
                            txt = self.grades[r][c]
                            self.grid[r][c] = Label(self.gridFrame, text=txt, relief=FLAT)
                    # elif c == abs(1 - self.col):
                    #     txt = "Update "+str(r)+":"+str(c)
                    #     updVar = self.grid[r][7].get()
                    #     self.grid[r][c] = Button(self.gridFrame, text=txt, command=lambda: self.updateGrade(updVar, self.grades[r][0]))
                    else:
                        txt = ""
                        self.grid[r][c] = Label(self.gridFrame, text=txt, relief=FLAT)
                    self.grid[r][c].grid(row=r+1, column=c, ipadx=10, ipady=5, sticky=W)

        self.gridFrame.update()
        gridHeight = self.gridFrame.winfo_height()
        gridWidth = self.gridFrame.winfo_width()

        self.master.create_window(0, 0, window=self.gridFrame, anchor=NW)
        self.master.config(yscrollcommand=vScrbar.set, xscrollcommand=hScrbar.set, scrollregion=(0, 0, gridWidth, gridHeight))

    def recreateFrame(self, event):
        self.setActModule(modCombobox.get)
        self.gridFrame.destroy()
        self.dataGrid()

    #def updateGrade(self, newGrade, gradeID):
    def updateGrade(self):
        dataPush = []
        i = 0
        for row in self.grid:
            print(i, row[0], row[7].get()  )
            #dataPush.append( ( int( row[0]['text'] ), int( row[7].get() ) ) )

            i+=1
        #print(dataPush)


        #print("UPDATE start for: " + str(newGrade) +" for "+ str(gradeID))
        #self.cursor.execute("UPDATE grade SET grade=? WHERE id=?", (newGrade, gradeID))
        #self.conn.commit
        #self.recreateFrame(1)



##########################################################################
# def recreateFrame():
#     print(modCombobox.get())

#########################################################
# draw GUI
root = Tk()
root.update()

#mainFrame = Frame(root, width=768, height=576)
mainFrame = Frame(root)
mainFrame.pack(side=LEFT, fill=BOTH, expand=1)

#############################################
# add topFrame to mainFrame
topFrame = Frame(mainFrame)
topFrame.config(height=200, relief=RAISED, borderwidth=1, padx=10, pady=15)
topFrame.pack(side=TOP, fill=X, expand=False)

#add canvas to mainFrame
mainCanvas = Canvas(mainFrame)
mainCanvas.pack(side=LEFT, fill=BOTH, expand=True)

#########################################################
# instantiate class
dataGrid = updateGradesClass("st81623", mainCanvas)

# add drop down list to frame
# get all modules related to teacherID in to an array
# on select refresh (update()) frame
modCombobox = ttk.Combobox(topFrame, textvariable=dataGrid.moduleIDs)
modCombobox["values"] = dataGrid.moduleIDs
modCombobox.bind("<<ComboboxSelected>>", dataGrid.recreateFrame)
modCombobox.pack(side=LEFT)

updateButton = Button(topFrame, text="Update all", command=dataGrid.updateGrade)
updateButton.pack(side=RIGHT)

#add scrollbar to mainFrame
vScrbar = Scrollbar(mainFrame, orient=VERTICAL)
vScrbar.pack(side=RIGHT, fill=Y)
hScrbar = Scrollbar(mainFrame, orient=HORIZONTAL)
hScrbar.pack(side=BOTTOM, fill=X)

#############################################
# add header to grid
# fixed header set for
#############################################
#dataGrid.setMaster(mainCanvas)
dataGrid.dataGrid()

#link scrollbar to canvas
vScrbar.config(command=mainCanvas.yview)
hScrbar.config(command=mainCanvas.xview)

#############################################
# add bottom Frame to mainFrame
# frame to UPDATE new record to DB
midFrame = Frame(mainFrame)
midFrame.pack(side=BOTTOM, fill=X, expand=False)

root.geometry("800x600")
root.mainloop()


#class called by combo box command, and the default is the first on list
# variables
#   active module
#   active set
#   or active module/set
# function to fetch data, set variables, row, col, sets, whatever
# function to draw grid
# try deleting frame by deleting this/class/object

# how to make scroll work with a canvas:
# Create a canvas widget and associate the scrollbars with that widget. Then, into that canvas embed the frame
# that contains your label widgets. Determine the width/height of the frame and feed that into the
# canvas scrollregion option so that the scrollregion exactly matches the size of the frame.
# the most important part is to call
# canvas.create_window(0, 0, window=<the object/frame you want to bind to canvas>, anchor=NW)
# otherwise the frame will not scroll with the canvas

# db queries
#cursor.execute("SELECT * FROM student")
#cursor.execute("SELECT count(*) FROM student")
#cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# sample data from DBv2
# (1, 'st78598', 'Mr', 'Nielsen', 'Kendrick', '', 'p@ssword')
# (2, 'st37935', 'Ms', 'Riddle', 'Johanna', '', 'p@ssword')
# (3, 'st80293', 'Mr', 'Bernard', 'Calvin', '', 'p@ssword')
# (4, 'st38097', 'Ms', 'Bridges', 'Danielle', '', 'p@ssword')
# (5, 'st81623', 'Mr', 'Bernard', 'Tomas', '', 'p@ssword')

# select column1 from table1
#    inner join table2 on table1.column = table2.column
#    where table2.column=0
