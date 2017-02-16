# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from dBhandler import *


if __name__ == "__main__":

    print("Hello World")

    # this file shall contain all the core code created by David
    # all the rest should be in seperate .py files in the project root folder
    # to use them, simply import then without the .py extension
    # just as the DBhandler module:
    # from dBhandler import *

    # ++++++++++++++++++  DB ++++++++++++++++++
    #for DB use, UNcomment the next line for sample data from tables
    #
    # testQueries()

    #to retrieve password for a certain user (student/teacher), the ID of these two groups are slightly different, and
    # need to be reworked later
    # the code checks the forst two char of the input argument to decide, then it returns the plain password as is.
    # argument parameter string (see below)
    #
    # print( retrievePW("17159305507") )
    # >>> p@ssword
    #
    # to use ONLY this function simply add the import line to top of your module file:
    # from dBhandler import retrievePW
    #
    # if want to import all use
    # from dBhandler import *