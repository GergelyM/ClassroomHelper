#imports for GUI
from tkinter import *
from tkinter import ttk

# imports for authentication need to be added in this form
from LoginHandlerClass import *
from activeUserClass import *
from updateGradesView import *


#datato test the login functions, more can be found in db_README.txt on GIT
# st78598
# 1733675
# p@ssword

# Login gui done by Gary, please do not remove comments, and all changes must be commented
# in this file and through GIT commit message if happened
##################################################################################
# Start of login GUI with authentication calls and returns
#

# instantiate the user container class, to hold and pass
# the active user's info to subsequent functions
activeUser = activeUserClass()

#functions and methods
def setSBarText(txt):
    setText = "   >>>  "+txt
    statusBar.config(text=setText)

def closeToplevel():
    print("Login done.")
    login.destroy()

def callLoginHandlerClass(uid, upw):
    # instantiate LoginHandler Class
    loginHandler = LoginHandler(uid, upw)
    print("loginHandler instance created")
    #activeUser.setUpObject(uid)
    print(loginHandler.loggedOn)  # loginHandler.loggedOn either False or the userID
    if loginHandler.loggedOn != False:
        #close window, set the User Class to hold user ID
        #print("loginHandler.loggedOn not False")
        activeUser.setUpObject(uid)
        print("activeUser object initialised")
        setSBarText(loginHandler.loginMessage)
        print("statusBar string updated")
        #closeToplevel()
        print("login destroyed")
    elif loginHandler.loggedOn == False:
        # should limit the tries later (no. of cases when login class returns False)
        setSBarText(loginHandler.loginMessage)
    # consider to kill Login object (authreturn)

#lambda event, name=button8.getLabel(): self.onButton(event, name)

#GUI generators

root = Tk()
#Window header text / window name
root.wm_title("Login")
#set min size of the window
root.minsize(width=800, height=600)
root.geometry("+200+200")
#window status bar
statusBar = Label(root, text="", bd=1, relief=GROOVE, anchor=W)
#relief is the simulated 3D effect: FLAT,RAISED,SUNKEN,GROOVE,RIDGE
#anchors are used to define where text is positioned relative to a reference point
statusBar.pack(side=BOTTOM, fill=X)

login = Toplevel(root)
login.wm_title("Login")
login.geometry("+280+280")

top1LabelUid = Label(login, text="User ID")
top1LabelUid.grid(row=1, pady=10, sticky=E)
top1LabelUpw = Label(login, text="Password")
top1LabelUpw.grid(row=2, pady=10, sticky=E)

top1EntryUid = Entry(login)
top1EntryUid.grid(row=1, column=1, columnspan=2, padx=5)
top1EntryUpw = Entry(login, show="*")
top1EntryUpw.grid(row=2, column=1, columnspan=2)

top1Button1 = Button(login, text="Cancel", command=closeToplevel)
top1Button1.grid(row=3, column=1, pady=10)
top1Button2 = Button(login, text="Login", command=lambda: callLoginHandlerClass( top1EntryUid.get(), top1EntryUpw.get() ))
top1Button2.grid(row=3, column=2)

login.attributes('-topmost', True) #brings toplevel window to the top
login.focus_force()  #gives focus to toplevel window
login.grab_set() #disables main window until toplevel closed or given back by login.grab_release()
root.wait_window(login)

#
# Login window code ends here.
##################################################################################
# Main window content starts here. This part of the code can be changed and reused freely.
#

# left frame
# holds all the buttons
menuFrame = Frame(root, width=200, background="gray", padx=10, pady=10)
menuFrame.pack(side=LEFT, fill=Y, expand=False, padx=3, pady=3)

# right frame
# holds the temporary frame with specific content
contentFrame = Frame(root, background="white")
contentFrame.pack(side=RIGHT, fill=BOTH, expand=True)

# label above buttons
leftFrameLabel = Label(menuFrame, justify=LEFT, text="Logged on as:\n" + activeUser.getFullname() + "\n")
leftFrameLabel.pack(fill=X, padx=3, pady=3)

#########################################################
def createUpgradeGrades():
    tempFrame = Frame(contentFrame)
    tempFrame.pack(side=RIGHT, fill=BOTH, expand=True)
    dataGrid = updateGradesClass(activeUser.getUID(), tempFrame)

#########################################################

# generate buttons dependent on
if activeUser.getType() == "teacher":
    button0 = Button(menuFrame, text='Grades of all students')
    button0.config(command=lambda: setSBarText("Grades"))
    button0.config(height=2)
    button0.pack(fill=X, padx=3, pady=3)
    button0.bind("<Enter>", lambda _: setSBarText("Grades of sets"))
    button0.bind("<Leave>", lambda _: setSBarText(""))

    button1 = Button(menuFrame, text='Update grades')
    # instantiate updateGradesView: dataGrid = updateGradesClass("st81623", root)
    button1.config(command=lambda: createUpgradeGrades() )
    button1.config(height=2)
    button1.pack(fill=X, padx=3, pady=3)
    button1.bind("<Enter>", lambda _: setSBarText("Update grades for students"))
    button1.bind("<Leave>", lambda _: setSBarText(""))

    button2 = Button(menuFrame, text='Grades of one student')
    button2.config(command=lambda: setSBarText("Grades of one student"))
    button2.config(height=2)
    button2.pack(fill=X, padx=3, pady=3)
    button2.bind("<Enter>", lambda _: setSBarText("Grades for one student"))
    button2.bind("<Leave>", lambda _: setSBarText(""))

    button3 = Button(menuFrame, text='List attendance')
    button3.config(command=lambda: setSBarText("Grades"))
    button3.config(height=2)
    button3.pack(fill="x", padx=3, pady=3)
    button3.bind("<Enter>", lambda _: setSBarText("List attendance"))
    button3.bind("<Leave>", lambda _: setSBarText(""))

    button4 = Button(menuFrame, text='Tick off attendance')
    button4.config(command=lambda: setSBarText("Grades"))
    button4.config(height=2)
    button4.pack(fill="x", padx=3, pady=3)
    button4.bind("<Enter>", lambda _: setSBarText("Tick off attendance"))
    button4.bind("<Leave>", lambda _: setSBarText(""))

    button5 = Button(menuFrame, text='Reports')
    button5.config(command=lambda: setSBarText("Grades"))
    button5.config(height=2)
    button5.pack(fill="x", padx=3, pady=3)
    button5.bind("<Enter>", lambda _: setSBarText("See reports"))
    button5.bind("<Leave>", lambda _: setSBarText(""))

elif activeUser.getType() == "student":
    button6 = Button(menuFrame, text='See my grades')
    button6.config(command=lambda: setSBarText("Grades"))
    button6.config(height=2)
    button6.pack(fill="x", padx=3, pady=3)
    button6.bind("<Enter>", lambda _: setSBarText("See my grades"))
    button6.bind("<Leave>", lambda _: setSBarText(""))

menuFrame.update()
root.mainloop()

# button.state( ["disabled"] )
# button.instate( ["disabled"] )  #returns true/false depends of the state of button widget
# button.state( ["!disabled"] )



# hook main window to the event handler loop
#
#
# def main():
#     root = Tk()
#     app = Demo1(root)
#     root.mainloop()
#
# if __name__ == '__main__':
#     main()