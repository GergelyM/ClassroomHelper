import sqlite3
from tkinter import *
from tkinter import ttk
import sqlite3
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
    conn = sqlite3.connect("db/crDBv2W10Demo.db")
    cursor = conn.cursor()
    grades = None
    # [[element] * numcols] * numrows
    #actModule = ""

    def __init__(self, teacherID, master):
        self.master = master
        #self.gridFrame = Frame(self.master)
        self.teacherID = teacherID
        self.dbFetch()
        self.moduleIDs = []
        #self.setPerModule = []
        for item in self.grades:
            setPerMtxt = str(item[4]) + " / " + str(item[1])
            if setPerMtxt not in self.moduleIDs:
                self.moduleIDs.append(setPerMtxt)
        # print(self.moduleIDs)
        # for item in self.grades:
        #     if item[4] not in self.moduleIDs:
        #         self.moduleIDs.append(item[4])
        # self.actModule = self.moduleIDs[0]
        self.actModule = self.retrieveModuleID( self.moduleIDs[0] )
        # print( self.actModule )
        self.col = len(self.grades[0])
        self.row = len(self.grades)
        self.grid = [[0] * (self.col+1)] * (self.row + 1) # +1 because of header

    def setActModule(self, actMod):
        self.actModule = actMod

    def retrieveModuleID(self, setPerModule):
        return setPerModule[0:6]

    def retrieveModuleInfo(self):
        theModule = [self.actModule]
        self.cursor.execute("SELECT * FROM module WHERE moduleID=?", theModule)
        fetchData = self.cursor.fetchone()



    def dbFetch(self):
        #tID = "st81623"
        thisYear = str(time.strftime("%Y"))  # 4 digit year
        bondQ = [self.teacherID, thisYear]
        self.cursor.execute("SELECT * FROM groupset INNER JOIN grade ON groupset.groupsetID=grade.groupsetID "
                       "WHERE groupset.teacherID=? AND groupset.year=? ORDER BY groupsetID", bondQ)
        self.grades = self.cursor.fetchall()
        #return grades

        # for i in self.grades:
        #     print(i)

        #print(self.grades)
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
    # todo-Gary DONE
    ###################################################################

    def dataGrid(self):
        # create frame to encapsulate
        self.gridFrame = Frame(self.master)
        self.gridFrame.pack(side=LEFT, fill=BOTH, expand=True)
        setPerModule = modCombobox.get()
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
                    elif fieldsToShow[c] is not None:
                        if c == fieldToEdit:
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
        self.master.create_window(0, 0, window=self.gridFrame, anchor=NW)

        # set scroll region to actual frame size
        self.gridFrame.update()
        gridHeight = 20 + self.gridFrame.winfo_height()
        gridWidth = self.gridFrame.winfo_width()
        self.master.config(yscrollcommand=vScrbar.set, xscrollcommand=hScrbar.set)
        self.master.config(scrollregion=(0, 0, gridWidth, gridHeight))

    #redraw the frame after modify
    def recreateFrame(self, event):
        actMod = self.retrieveModuleID( modCombobox.get() )
        self.setActModule( actMod )
        # print( actMod  )
        self.gridFrame.destroy()
        self.dbFetch()
        self.dataGrid()
        self.master.update()

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

    # lambda argument_list: expression



#########################################################

# draw GUI
# create window
root = Tk()
root.update()

# main frame, placeholder for the data grid
mainFrame = Frame(root)
mainFrame.pack(side=LEFT, fill=BOTH, expand=True)

#############################################
# add topFrame to mainFrame
# frame with module select, ?set select?, module info, etc.
topFrame = Frame(mainFrame)
topFrame.config(height=200, relief=RAISED, borderwidth=1, padx=10, pady=15)
topFrame.pack(side=TOP, fill=X, expand=False)

# add canvas to mainFrame
# to sort out scroll for data grid
mainCanvas = Canvas(mainFrame)
mainCanvas.pack(side=LEFT, fill=BOTH, expand=True)

#########################################################
# instantiate class
# the actual data grid
# teachers with more than one set: st82277, st81623

dataGrid = updateGradesClass("st81623", mainCanvas)

# add drop down list to frame
# get all modules related to teacherID in to an array
# on select refresh (update()) frame
modCombobox = ttk.Combobox(topFrame, textvariable=dataGrid.moduleIDs)
modCombobox["values"] = dataGrid.moduleIDs
modCombobox.bind("<<ComboboxSelected>>", dataGrid.recreateFrame)
modCombobox.pack(side=LEFT)

#set combo box for further filtering
# setCombobox = ttk.Combobox(topFrame, textvariable=dataGrid.moduleIDs)
# setCombobox["values"] = dataGrid.moduleIDs
# setCombobox.bind("<<ComboboxSelected>>", dataGrid.recreateFrame)
# setCombobox.pack(side=LEFT)

#create Label for module info



# updateButton = Button(topFrame, text="Update all", command=dataGrid.updateGrade)
# updateButton.pack(side=RIGHT)

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
# (4, 'st38097', 'Ms', 'Bridges', 'Danielle', '', 'p@ssword')
# (5, 'st81623', 'Mr', 'Bernard', 'Tomas', '', 'p@ssword')

# select column1 from table1
#    inner join table2 on table1.column = table2.column
#    where table2.column=0
