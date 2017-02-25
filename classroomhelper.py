# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from dbHandler import *

if __name__ == "__main__":

    # this file shall contain all the core code created by David
    # all the rest should be in seperate .py files in the project root folder
    # to use them, simply import then without the .py extension
    # just as the DBhandler module:
    # from dBhandler import *

    # ++++++++++++++++++  DB ++++++++++++++++++
    # setup the DB connection [crDB] with a simple Class, too keep it alive through the lifetime of the app/class
    # you should write your functions in a form that you pass the db connection into them as argument,
    # eg: funtion(crDB):
    # so this way it's not necessary to open a new connection every time you want to interact with the db
    # NOTE: because of the class you have to create the cursor slightly different, just
    #       instead of
    #       crDB.cursor() you want use
    #       crDB.cursor
    # without the '()'
    crDB = DbConn("db/crDB.db")

    # initDB(crDB)




    # hint, uncomment the next line for sample data from tables
    #testQueries(crDB)

    # to retrieve password for a certain user (student/teacher), the ID of these two groups are slightly different, and
    # need to be reworked later
    # the code checks the forst two char of the input argument to decide, then it returns the plain password as is.
    # argument parameter string (see below)
    #
    print( retrievePW("17159114703") )
    # this will return:
    # >>> p@ssword
    # From the record where the unique student ID is: 17159114703
    # the actual record is: (1, '17159114703', '', 'Loretta', 'Staley', '14/03/1997', 'p@ssword')
    # the raw form of the return of the query is a one item list with a one item tuple in it.
    #
    # to use ONLY this function in your python file simply add the import line to top of your module file:
    #from dBhandler import retrievePW
    #
    # if want to import all use
    #from dBhandler import *