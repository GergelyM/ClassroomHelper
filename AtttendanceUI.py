'''Warning, lots of testing, lots of experimenting to find the best way of doing things as well as'''

import tkinter as tk

def submit():
    print("Submit button pressed")
    #for x in range (1, 7):
     #   ifPresent = "checkCmd" + str(x).get()
      #  print("Student " + x + " has value: " + ifPresent)
    print(test1.get())
    print(test2.get())
    print(test3.get())
    print(test4.get())
    print(test5.get())
    
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

'''for x in range (1, 7):
    studentLabel = "label" + str(x)
    studentCheckbox = "checkbox" + str(x)
    print(studentLabel)
    #checkCmd = tk.IntVar()
    #test1 = checkCmd + str(x)
    test1 = tk.IntVar()
    #checkCmd.set(0)
    studentLabel = tk.Label(frame2, text="Student: " + str(x)).grid(column=0,row = x)
    studentCheckbox = tk.Checkbutton(frame2, text="Student: " + str(x), variable=test1, onvalue=1, offvalue=0).grid(column = 1, row = x)
'''

button1 = tk.Button(frame3, text="Submit", command=submit) # Search button
button1.pack(side='left', padx=5, pady=10) # Asthetic but necessary

test1 = tk.IntVar()
checkbox1 = tk.Checkbutton(frame2, text="Student 1", variable=test1, onvalue=1, offvalue=0).grid(column = 1, row = 1)
test2 = tk.IntVar()
checkbox2 = tk.Checkbutton(frame2, text="Student 2", variable=test2, onvalue=1, offvalue=0).grid(column = 1, row = 2)
test3 = tk.IntVar()
checkbox3 = tk.Checkbutton(frame2, text="Student 3", variable=test3, onvalue=1, offvalue=0).grid(column = 1, row = 3)
test4 = tk.IntVar()
checkbox4 = tk.Checkbutton(frame2, text="Student 4", variable=test4, onvalue=1, offvalue=0).grid(column = 1, row = 4)
test5 = tk.IntVar()
checkbox5 = tk.Checkbutton(frame2, text="Student 5", variable=test5, onvalue=1, offvalue=0).grid(column = 1, row = 5)

root.mainloop() # Run 
