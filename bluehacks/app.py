from flask import Flask, render_template ,url_for ,request,redirect,session,logging,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.static_folder = 'static'
app.TEMPLATES_AUTO_RELOAD=True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'anonymouseisreal'
engine = create_engine('sqlite:///database.db')
db=scoped_session(sessionmaker(bind=engine))

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
    if request.method=="POST":

        email=request.form['email']
        password = request.form['password']
        usernamedata=db.execute("SELECT email FROM accounts WHERE email=:email",{"email":email}).fetchone()
        uresult = db.fetachall()
        passworddata=db.execute("SELECT password FROM accounts WHERE email=:email",{"password":password}).fetchone()
        presult = db.fetchall()

        if usernamedata is None:
            flash("No username","danger")
            return render_template('login.html')
        else:
            for passwor_data in passworddata:
                if sha256_crypt.verify(password,passwor_data):
                    session["log"]=True
                    flash("You are now logged in!!","success")
                    return redirect(url_for('hello')) #to be edited from here do redict to either svm or home
                else:
                    flash("incorrect password","danger")
                    return render_template('login.html')
    return render_template('login.html')

@app.route('/register',methods=["POST","GET"])
def register():
    if request.method == 'POST':
        fname=request.form['fname']
        email=request.form['email']
        address=request.form['address']
        contact=request.form['contact']
        username=request.form['username']
        password=request.form['password']
        secure_password=sha256_crypt.encrypt(str(password))
        usernamedata=db.execute("SELECT email FROM accounts WHERE email=:email",{"email":email}).fetchone()
    
        if usernamedata==None:
                if password==confirm:
                    db.execute("INSERT INTO accounts(fname,email,address,contact,username,password) VALUES(:fname,:email,:address,:contact,:username,:password)",
                        {"fname":fname,"email":email,"address":address,"contat":contact,'username':username,'password':secure_password})
                    db.commit()
                    flash("You are registered and can now login","success")
                    return redirect(url_for('login'))
                else:
                    flash("password does not match","danger")
                    return render_template('register.html')
        else:
            flash("user already existed, please login or contact admin","danger")
            return redirect(url_for('login'))
    return render_template('register.html')
    
if __name__ == "__main__":
    app.run(debug=True, port=6969)
    
    