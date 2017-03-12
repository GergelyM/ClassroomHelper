import tkinter as tk

def submit():
    print("Submit button pressed")
    #for x in range (1, 7):
     #   ifPresent = "checkCmd" + str(x).get()
      #  print("Student " + x + " has value: " + ifPresent)
    print(checkCmd.get())
    
root = tk.Tk()
root.geometry("%dx%d+%d+%d" % (630, 250, 100, 20))
root.title("Attendance Register")

frame1 = tk.Frame(root)
frame1.pack()
frame2 = tk.Frame(root)
frame2.pack()
frame3 = tk.Frame(root)
frame3.pack()

introLabel1 = tk.Label(frame1, text="Student name").grid(column = 0,row = 0)
introLabel2 = tk.Label(frame1, text="Present?").grid(column = 1,row = 0)

#checkCmd = tk.IntVar()
#checkCmd.set(0)

for x in range (1, 7):
    studentLabel = "label" + str(x)
    studentCheckbox = "checkbox" + str(x)
    print(studentLabel)
    #checkCmd = tk.IntVar()
    "test" + str(x) = checkCmd + str(x)
    #test1 = tk.IntVar()
    #checkCmd.set(0)
    studentLabel = tk.Label(frame2, text="Student: " + str(x)).grid(column=0,row = x)
    studentCheckbox = tk.Checkbutton(frame2, text="Student: " + str(x), variable=test1, onvalue=1, offvalue=0).grid(column = 1, row = x)

button1 = tk.Button(frame3, text="Submit", command=submit) # Search button
button1.pack(side='left', padx=5, pady=10) # Asthetic but necessary


root.mainloop() # Run 
