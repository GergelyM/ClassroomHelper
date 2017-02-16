userDB = [{"id":"15077697", "surname":"Morp", "name":"David", "modules":["U08008", "U08007"], "dob":"01-01-99", "grade":"100"},
          {"id":"12345678", "surname":"Champion","name":"Bob", "modules":["U08008", "U08007"], "dob":"01-01-55", "grade":"40"},
          {"id":"18745678", "surname":"Lightfoot","name":"David", "modules":["U08009", "U08007"], "dob":"01-01-25", "grade":"70"},
          {"id":"12675678", "surname":"Will","name":"Cook", "modules":["U08008", "U08009"], "dob":"01-01-57", "grade":"80"}]

def displayGrades(module, userDB):
    for user in userDB: #go through all the students
        if module in user["modules"]: #if they are taking the module requested
            print(user["id"], '%10s' % user["surname"], '%5s' %user["name"], user["dob"],'%3s' % user["grade"])


displayGrades("U08008", userDB)
