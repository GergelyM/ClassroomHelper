from tkinter import *
from IndividualReport import *

#Function to call individual report class and pass data
def callIndividualReport(id, year):
    a = individualReport(id, year)
    a.createReport()

    #Create a report and deletes unwanted symbols
    IndividualReport = a.createReport()
    IndividualReport = str(IndividualReport)
    IndividualReport = IndividualReport.replace("'","")
    IndividualReport = IndividualReport.replace(",","")
    IndividualReport = IndividualReport.replace(")", "")
    IndividualReport = IndividualReport.replace("(","")
    IndividualReport = IndividualReport.replace('"',"")

    #Close the first window
    root.destroy()

    #Create second window
    root2 = Tk()
    master2 = root2
    master2.wm_title("Report")

    #Print report on the second window
    report = Label(master2, text = "Report: ")
    report.pack()
    report["text"] = IndividualReport


root = Tk()

master = root
master.wm_title("Individual Report")

#Creates labels
labelID = Label(master, text="Student ID").grid(row=0, sticky=E)
labelPassword = Label(master, text="Year").grid(row=1, sticky=E)

#Creates input entries
EntryID = Entry(master)
EntryID.grid(row=0, column=1)
EntryYear = Entry(master)
EntryYear.grid(row=1, column=1)

#Creates a button
button = Button(master, text="Get report", command=lambda: callIndividualReport(EntryID.get(), EntryYear.get()) )
button.grid(row=2, column=2)

root.mainloop()