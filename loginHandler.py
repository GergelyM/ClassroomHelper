### Author: Salik
### Trasferred from Pulled project file by Gary

# it would be a bit more efficient if you would use a single data query for the user by login input name
# in that way the code could decide if the input name exists in the DB, 
# and if it does, then that the stored password is equal to the user input
# I will write the SQL statement here so you can just fit it in your code.
# well practically I'll make a variable with the db field values above.

# for test purposes only
from dBhandler import *

#for test purposes only

crDB = DbConn("db/crDB.db")

#TODO-Gary write the sql statements for the login

# to make it simple I'll write a new function what gets the data from DB
def fetchData(user):
    if user[0:1].isnumeric():   # check if the first two characters are numeric = student ID
        newSq = "SELECT studentPassword FROM student WHERE studentID = '" + user + "'"
    if user[0:1] == "st":
        newSq = "SELECT teacherPassword FROM teacher WHERE teacherID = '" + user + "'"

    return crDB.query(newSq)    # possible values : empty list [] OR password string

# to get back the output, it needs to be handled as a list of tuples [(),()...]
# in this case it is a list of one tuple
# print( fetchData("17159114703") )
# >>> [('p@ssword',)]

# purely for test purposes, when expecting multiple list item returned
for row in fetchData("17159114703"):
    print (row[0])
# >>> p@ssword

# purely for test purposes, in any other cases
testVar = fetchData("17159114703")
print(testVar[0][0])
# >>> p@ssword

def login():
    # 1st list - Student's ID
    # 2nd list - Student's passwords
    # 3rd list - Teacher's ID
    # 4th list - Teacher's passwords
    users = [["00000000001", "00000000002", "00000000003", "00000000004"], ["1234qwer", "9876asdf", "777000", "010101"], ["00000000005", "00000000006"], ["909090", "8080"]]

    login = input("Enter login: ")
    status = ""

    # at this point the code shouldn't compare anything, it's a security issue
    # having the code checking if a user exist before getting the password
    # makes it easy to guess a user, and then the password seperately
    # the best way would be get both data in (uers/password)
    # then compare them to the db fetch
    # and then on 'fail' ask for new input in a loop if you fancy
    # maybe an exeption handler 'try:except' would do the work a lil' better
    while login not in users[0] and login not in users[2]:
        login = input("Incorrect, enter login: ")

    # Check if user logged as a student or a teacher
    # Returns "s" if logged as a student
    # Returns "t" if logged as a teacher
    if login in users[0]:
        status = "s"
        password = input("Enter password: ")

    elif login in users[2]:
        status = "t"
        password = input("Enter password: ")
    else:
        print("Incorrect login")

    # Check if login and password match
    # Returns "s" if logged as a student
    # Returns "t" if logged as a teacher
    # Returns "f" if login failed
    if status == "s":
        x = users[0].index(login)
        if password == users[1][x]:
            print("Logged as a student")
            return status
        else:
            print("Incorrect password")
            status = "f"
            return status

    if status == "t":
        y = users[2].index(login)
        if password == users[3][y]:
            print("Logged as a teacher")
            return status
        else:
            ("Incorrect password")
            status = "f"
            return status
