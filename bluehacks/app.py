from flask import Flask, render_template ,url_for ,request
from flask_cors import CORS
from os import path
import sqlite3 as sql

app = Flask(__name__)
CORS(app)
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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register',methods=["POST","GET"])
def register():
    if request.method == "GET":
        pass
    if request.method == "POST":
        try:
            names = request.form['name']
            email = request.form['email']
            addr = request.form['addr']
            cn = request.form['cn']
            username = request.form['username']
            pass1 = request.form['pass1']
            pass2 = request.form['pass2']
        
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO register(names,email,addr,cn,username,pass1,pass2) VALUES(?,?,?,?,?,?,?,?)",(names,email,addr,cn,username,pass1,pass2))
                con.commit()
                msg = "Record Successfully added "
        except:
            con.rollback()
            msg = "Error Inserting Operation"
        finally:
            return render_template('register.html')
            con.close()
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True, port=6969)
    
    