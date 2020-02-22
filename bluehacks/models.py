import sqlite3
from os import path
from datetime import date
from flask import Flask, render_template ,url_for ,request,redirect

ROOT = path.dirname(path.relpath(__file__))

def create_account(name, email, address, contact, username, password):
    con = sqlite3.connect(path.join(ROOT,'database.db'))
    cur = con.cursor()
    cur.execute('insert into accounts (fullname ,username, email, contact, pass, usertype, datecreated) values(?,?,?,?,?,?,?)',(name,username, email, contact, password, 'user', str(date.today())))
    con.commit()
    con.close()

def login(email,password):
    con = sqlite3.connect(path.join(ROOT,'database.db'))
    cur = con.cursor()
    cur.execute('select * from accounts where email = ? and pass = ?',(email,password))
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows