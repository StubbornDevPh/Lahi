from flask import Flask, render_template ,url_for ,request,redirect
from os import path
import sqlite3
from datetime import date
import models

app = Flask(__name__)
app.TEMPLATES_AUTO_RELOAD=True

@app.route('/', methods=['POST','GET'])
def index():
    
    if request.method == 'GET':
        pass

    if request.method == "POST":
        pass

    return render_template('index.html')
#index then feed
#about
#places
#option search place
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/places')
def places():
    return render_template('places.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
    #code this
    return render_template('login.html')

@app.route('/register',methods=["POST","GET"])
def register():
    if request.method=='GET':
        pass
    if request.method=='POST':
        try:
            name = request.form.get('fname')
            email = request.form.get('email')
            address = request.form.get('address')
            contact = request.form.get('contact')
            username = request.form.get('username')
            password = request.form.get('password')
            models.create_account(name, email, address, contact, username, password)
        except:
            flash('error')
        finally:
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/validate/num')
def validate(num):
    if(num==0):
        return 'no acc'
    elif(num==1):
        return 'acc match'

if __name__ == "__main__":
    app.run(debug=True, port=6969)
    
    