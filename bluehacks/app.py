from flask import Flask, render_template ,url_for ,request,redirect,session,logging,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

app = Flask(__name__)
app.static_folder = 'static'
app.TEMPLATES_AUTO_RELOAD=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'anonymouseisreal'

db = SQLAlchemy(app)

class Accounts(db.Model):
    id = db.Column('user_id', db.Integer, primary_key = True)
    fname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    address = db.Column(db.String(100))
    contact = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

def __init__(self, fname, email, address, contact, username, password):
    self.fname = fname
    self.email = email
    self.address = address
    self.contact = contact
    self.username = username
    self.password = password

db.create_all()

@app.route('/', methods=['POST','GET'])
def index():
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
    if request.method == 'POST':
        Account = Accounts(fname=request.form['fname'], email=request.form['email'], address=request.form['address'], contact=request.form['contact'], username=request.form['username'], password=request.form['password'])
        db.session.add(Account)
        db.session.commit()
    return render_template('register.html')
    
if __name__ == "__main__":
    app.run(debug=True, port=6969)
    
    