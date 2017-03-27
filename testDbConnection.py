from dbHandler import *
import time

c = DbConn("db/crDBv2.db")
cur = c.cursor


# select everything from a table
cur.execute("SELECT * FROM student")

# count all rows in a table
cur.execute("SELECT count(*) FROM student")

# lists all tables in the DB
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
dataFetch = cur.fetchall()
print(dataFetch)

# selects all from table but limit the query to 3 hits
cur.execute("SELECT * FROM teacher LIMIT 3")
dataFetch = cur.fetchall()
print(dataFetch)

# selects all from table and order the query by field
cur.execute("SELECT * FROM grade ORDER BY studentID")
dataFetch = cur.fetchall()
print(dataFetch)

# returns the field info for table
cur.execute("PRAGMA table_info('groupset') ")
dataFetch = cur.fetchall()
print("groupset PRAGMA:")
print(dataFetch)

# a little bit more complicated query
# selects all records where teacherID and year from the groupset and grade tables joined by (on) groupsetID
thisYear = str(time.strftime("%Y"))  # 4 digit year
bondQ = ["st81623", thisYear]
cur.execute("SELECT * FROM groupset INNER JOIN grade ON groupset.groupsetID=grade.groupsetID WHERE groupset.teacherID=? AND groupset.year=? ORDER BY groupsetID", bondQ)
grades = cur.fetchall()
print(grades) #this will be a looooooong print on console