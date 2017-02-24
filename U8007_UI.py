'''As things stand i can not find a way to clear the label of the text currently in it
Will continue looking for a way to do it but if not I may need to change it to a different
form of text box.
That means that every time the program is run it can only search for one module then needs to be restarted

'''
import tkinter as tk

def select():
    textbox1.delete('1.0','99999999.0')
    titleModule = "Selected module is %s" % var.get() # Names the window
    theModule = var.get()
    root.title(titleModule) # Names the window
    selectedModule = str(theModule) 
    i = 0
    moduleList = [("222", 'StudentID 1', 'Name 2', "Surname 3", "DOB 4", "Grade 5"),("333", 'StudentID 6', 'Name 7', "Surname  8", "DOB 9", "Grade 10"),("444",'StudentID 11', 'Name 12', "Surname 13", "DOB 14", "Grade 15")] # Shortened to not include all modules just for ease
    for m in moduleList:
        if m[0] == selectedModule:
            textbox1.insert('1.0', m)
            #print(m)


root = tk.Tk()
root.geometry("%dx%d+%d+%d" % (600, 200, 100, 20))
root.title("Teacher module select")
var = tk.StringVar(root)

frame1 = tk.Frame(root)
frame1.pack()
frame2 = tk.Frame(root)
frame2.pack()
frame3 = tk.Frame(root)
frame3.pack()

label1 = tk.Label(frame2,text=("Module code" + "            " + "Student ID" + "                       " + "Name" + '                     ' + "Surname" + '                     ' + "DoB" + '                    ' + "Grade"),height=1, width=120)
label1.pack()
# initial value
var.set('Select Module') # Original text in drop down menu
choices = [222,333,444,555,666,777] # Module code choices
option = tk.OptionMenu(frame1, var, *choices) # Drop down menu
option.pack(side='left', padx=5, pady=5) # Asthetic but necessary
button1 = tk.Button(frame1, text="Search", command=select) # Search button
button1.pack(side='left', padx=5, pady=10) # Asthetic but necessary

label2 = tk.Label(frame3, text="Module information goes here")
label2.pack()
   


#scrollbar = tk.Scrollbar(root)
#scrollbar.pack(side=RIGHT, fill=Y)

textbox1 = tk.Text(frame3,)
textbox1.insert('1.0', "Hello")
#textbox1.insert(END, "Bye Bye")
textbox1.pack()

root.mainloop() # Run 