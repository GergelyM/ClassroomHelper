### Author: Salik
### Trasferred from Pulled project file by Gary

# it would be a bit more efficient if you would use a single data query for the user by login input name
# in that way the code could decide if the input name exists in the DB,
# and if it does, then that the stored password is equal to the user input
# I will write the SQL statement here so you can just fit it in your code.
# well practically I'll make a variable with the db field values above.

from dBhandler import *

crDB = DbConn("db/crDB.db")

def fetchData(user):
    global newSq
    if user[0:1].isnumeric():
        newSq = "SELECT studentPassword FROM student WHERE studentID = '" + user + "'"
    if user[0:1] == "st":
        newSq = "SELECT teacherPassword FROM teacher WHERE teacherID = '" + user + "'"
    return crDB.query(newSq)

# to get back the output, it needs to be handled as a list of tuples [(),()...]
# in this case it is a list of one tuple
# print( fetchData("17159114703") )
# >>> [('p@ssword',)]


def login():
    global password
    loginID = input("Enter ID: ")
    loginPass = fetchData(loginID)
    loginPass = str(loginPass)
    loginPass = loginPass[1:]
    loginPass = loginPass[1:]
    loginPass = loginPass[1:]
    loginPass = loginPass[:-1]
    loginPass = loginPass[:-1]
    loginPass = loginPass[:-1]
    loginPass = loginPass[:-1]

    status = ""

# Check if user logged as a student or a teacher
# Returns "s" if logged as a student
# Returns "st" if logged as a teacher

    if loginID[0:1].isnumeric():
        status = "s"
        password = input(str("Enter password: "))
    elif loginID[0:1] == "st":
        status = "st"
        password = input(str("Enter password: "))
    else:
        print("Incorrect ID")

# Check if login and password match
# Returns "s" if logged as a student
# Returns "t" if logged as a teacher
# Returns "f" if login failed

    if  password == loginPass:
        print("Logged as a student")
        return status
    elif status =="st" and password == loginPass:
        print("Logged as a teacher")
        return status
    else:
        print("Incorrect password")
        status = "f"
        return status

print(login())
