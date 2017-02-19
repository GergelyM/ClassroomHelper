### Author: Salik
### Trasferred from Pulled project file by Gary

# it would be a bit more efficient if you would use a single data query for the user by login input name
# in that way the code could decide if the input name exists in the DB, 
# and if it does, then that the stored password is equal to the user input
# I will write the SQL statement here so you can just fit it in your code.
# well practically I'll make a variable with the field values above.

#TODO-Gary write the sql statements for the login

def login():
    # 1st list - Student's ID
    # 2nd list - Student's passwords
    # 3rd list - Teacher's ID
    # 4th list - Teacher's passwords
    users = [["00000000001", "00000000002", "00000000003", "00000000004"], ["1234qwer", "9876asdf", "777000", "010101"], ["00000000005", "00000000006"], ["909090", "8080"]]

    login = input("Enter login: ")
    status = ""

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
