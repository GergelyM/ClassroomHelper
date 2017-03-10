#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#FCK tinyDB, ditched for good, too complicated to be called "small and easy"

import sqlite3

class DbConn(object):
    def __init__(self, dbPath):  #object/class constructor, everything in __init__ will be called when a copy of the class being created
        self.connection = sqlite3.connect(dbPath)
        self.connection.execute('pragma foreign_keys = on')
        self.connection.commit()
        self.cursor = self.connection.cursor()

    def query(self, arg):
        self.cursor.execute(arg)
        data = self.cursor.fetchall()   # fetchall() makes possible to use 'list[n][k]' call on the fetched data directly
        self.connection.commit()
        #return self.cursor
        return data

    def __del__(self):
        self.connection.close()












