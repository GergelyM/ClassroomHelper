'''As things stand i can not find a way to clear the label of the text currently in it
Will continue looking for a way to do it but if not I may need to change it to a different
form of text box.
That means that every time the program is run it can only search for one module then needs to be restarted

'''
import tkinter as tk

def select():
    titleModule = "Selected module is %s" % var.get() # Names the window
    root.title(titleModule) # Names the window
    intVar = int(var.get()) # Maybe not necessary but was for my testing
    selectedModule = intVar - 1 
    moduleList = [(1, 'Text 1', 'Text 2'),(1, 'Text 3', 'Text 4'),(3,'Text 5', 'Text 6')] # Shortened to not include all modules just for ease
    for selectedModule in moduleList:
        label2 = tk.Label(frame3, text=moduleList[intVar-1])
        label2.pack()
        #print(moduleList[intVar-1]) -- Just a test line


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

label1 = tk.Label(frame2,text=("Student ID" + "--------" + "Name" + '--------' + "Surname" + '-------' + "DoB" + '---------' + "Grade"),height=1, width=120)
label1.pack()
# initial value
var.set('Select Module') # Original text in drop down menu
choices = [1,2,3,4,5,6] # Module code choices
option = tk.OptionMenu(frame1, var, *choices) # Drop down menu
option.pack(side='left', padx=5, pady=5) # Asthetic but necessary
button1 = tk.Button(frame1, text="Search", command=select) # Search button
button1.pack(side='left', padx=5, pady=10) # Asthetic but necessary
root.mainloop() # Run 