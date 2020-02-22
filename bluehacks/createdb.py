import sqlite3

con = sqlite3.connect('database.db')
print ("Opened database successfully")

con.execute('CREATE TABLE accounts (id INTEGER NOT NULL,username TEXT,email TEXT, contact TEXT, pass TEXT, usertype TEXT,datecreate DATE)')
print ("TABLE CONNECTED SUCCESSFULLY")
con.commit()
con.close()