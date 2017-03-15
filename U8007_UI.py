'''As things stand i can not find a way to clear the label of the text currently in it
Will continue looking for a way to do it but if not I may need to change it to a different
form of text box.
That means that every time the program is run it can only search for one module then needs to be restarted

Fixed - Gavin
'''

'''I added in some functions. I commented some stuff.
Sorry if is messy, it should make sense to you.If not PLEASE ASK.
It seems to be working BUT we need to two things:
1) Fix spacing/alignment
2) Remove the {} from each stirng in the output
Note: try with module M03010
It starting to come toghether :D
by David'''

teacherID = 'st82277' #Fixed teacher ID for now

#TODO Everyone make more dummy data in the DB

import tkinter as tk
import coreFunctionsSQL as core

def select():
    textbox1.delete('1.0','99999999.0')
    titleModule = "Selected module is %s" % var.get() # Names the window
    theModule = var.get()
    root.title(titleModule) # Names the window
    selectedModule = str(theModule)
    title, header, moduleList = core.displayGrades(selectedModule) #by David
    moduleList.append(header) #Add the header at the top of the list
    #i = 0
    #print(moduleList) #by David
    #moduleList = [("222", 'StudentID 1', 'Name 2', "Surname 3", "DOB 4", "Grade 5"),("333", 'StudentID 6', 'Name 7', "Surname  8", "DOB 9", "Grade 10"),("444",'StudentID 11', 'Name 12', "Surname 13", "DOB 14", "Grade 15")] # Shortened to not include all modules just for ease
    for m in moduleList:
        #if m[0] == selectedModule:
        txt = str(m)+"\n"   #endOfLine added after each line will sort the line issues for now
        textbox1.insert('1.0', txt)#by David
            #print(m)


root = tk.Tk()
root.geometry("%dx%d+%d+%d" % (630, 250, 100, 20))
root.title("Teacher module select")
var = tk.StringVar(root)

frame1 = tk.Frame(root)
frame1.pack()
frame2 = tk.Frame(root)
frame2.pack()
frame3 = tk.Frame(root)
frame3.pack()
headerGavin = "code" + "            " + "Student ID" + "                       " + "Name" + '                     ' + "Surname" + '                     ' + "DoB" + '                    ' + "Grade" #by David
headerDavid = '%15s' % "Student ID",  '%15s' % "Name", '%13s' % "Surname", '%15s' % "DoB", '%10s' % "Grade" #by David
#label1 = tk.Label(frame2,text=headerDavid,height=1, width=120) #by David
#label1.pack()
# initial value
var.set('Select Module') # Original text in drop down menu
choices = core.getModules(teacherID)#by David #[222,333,444,555,666,777] # Module code choices
option = tk.OptionMenu(frame1, var, *choices) # Drop down menu
option.pack(side='left', padx=5, pady=5) # Asthetic but necessary
button1 = tk.Button(frame1, text="Search", command=select) # Search button
button1.pack(side='left', padx=5, pady=10) # Asthetic but necessary

label2 = tk.Label(frame3, text="Module information goes here (see comment)")
#You can get modules info from core.getModuleInfo(selectedModule). Not sure how to make it update when a module is actually selected
label2.pack()
# just run label2.update() that should do - Gary


#scrollbar = tk.Scrollbar(root)
#scrollbar.pack(side=RIGHT, fill=Y)

textbox1 = tk.Text(frame3, width=78)
textbox1.insert('1.0', "Hello")
#textbox1.insert(END, "Bye Bye")
textbox1.pack()

root.mainloop() # Run 
