### Author: Salik
### Trasferred from Pulled project file by Gary

# it would be a bit more efficient if you would use a single data query for the user by login input name
# in that way the code could decide if the input name exists in the DB,
# and if it does, then that the stored password is equal to the user input
# I will write the SQL statement here so you can just fit it in your code.
# well practically I'll make a variable with the db field values above.

from dbHandler import *

#################################################################################################
# do not change this part, please!
#move everything to a login class

class LoginHandler(object):
        #class-wide shared variables
        crDB = DbConn("db/crDB.db")
        c = crDB.cursor


        def __init__(self):
         #python constructor method
            #object-level variables, unique to object
            self.userID = input("Enter ID: ")
            self.userPassword = input("Enter password: ")

        def readInput(self):
            self.userID = input("Enter ID: ")
            self.userPassword = input("Enter password: ")

        def fetchData(self):
            newSq = ""
            if self.userID[0:1].isnumeric():
                newSq = "SELECT studentPassword FROM student WHERE studentID = '" + self.userID + "'"
            if self.userID[0:2] == "st":
                newSq = "SELECT teacherPassword FROM teacher WHERE teacherID = '" + self.userID + "'"
            self.c.execute(newSq)
            fetchedPw = self.c.fetchone()[0]
            return fetchedPw

        def login(self):
            idInput = self.userID
            passInput = self.userPassword
            if (passInput != self.fetchData()):
                print("Login failed. Please try again.")
            elif passInput == self.fetchData():
                print("Authentication successful, please proceed. Or whatever.")
            return idInput

#################################################################################################
#just comment out these lines if you need to work on this file, but leave them as is, thanks

#uId = input("Enter ID: ")
#uPw = input("Enter password: ")
logi = LoginHandler()
print( logi.login() )

#################################################################################################


crDB = DbConn("db/crDB.db")
c = crDB.cursor

def fetchData(userID):
    #global newSq   # why is this global? an why is this here?
    newSq = ""
    if userID[0:1].isnumeric():
        newSq = "SELECT studentPassword FROM student WHERE studentID = '" + userID + "'"
    if userID[0:2] == "st":
        newSq = "SELECT teacherPassword FROM teacher WHERE teacherID = '" + userID + "'"
    c.execute(newSq)
    return c.fetchone()[0][0]

# to get back the output, it needs to be handled as a list of tuples [(),()...]
# in this case it is a list of one tuple
# print( fetchData("17159114703") )
# >>> [('p@ssword',)]
#print( fetchData("st147707702") )
#print( fetchData("17159114703") )

def login():
    #global password
    idInput = input("Enter ID: ")
    passInput = input("Enter password: ")
    while (passInput != fetchData(idInput)) :
        idInput = input("Enter ID: ")
        passInput = input("Enter password: ")
        if passInput != fetchData(idInput) :
            print("Login failed. Please try again.")
        elif passInput == fetchData(idInput):
            print("Authentication successful, please proceed. Or whatever.")
    return idInput

#print( login() )

    #loginPass = fetchData(loginID)
    # loginPass = str(loginPass)
    # loginPass = loginPass[1:]
    # loginPass = loginPass[1:]
    # loginPass = loginPass[1:]
    # loginPass = loginPass[:-1]
    # loginPass = loginPass[:-1]
    # loginPass = loginPass[:-1]
    # loginPass = loginPass[:-1]

    #status = ""

# Check if user logged as a student or a teacher
# Returns "s" if logged as a student
# Returns "st" if logged as a teacher
# both wrong

    # if loginID[0:1].isnumeric():
    #     status = "s"
    #     password = input(str("Enter password: "))
    # elif loginID[0:1] == "st":
    #     status = "st"
    #     password = input(str("Enter password: "))
    # else:
    #     print("Incorrect ID")

# Check if login and password match


# Returns "s" if logged as a student
# Returns "t" if logged as a teacher
# Returns "f" if login failed

    # if  password == loginPass:
    #     print("Logged as a student")
    #     return status
    # elif status =="st" and password == loginPass:
    #     print("Logged as a teacher")
    #     return status
    # else:
    #     print("Incorrect password")
    #     status = "f"
    #     return status

#print(login())
