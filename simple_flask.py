from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import argon2
from sqlalchemy import create_engine, inspect


app = Flask(__name__)
app.secret_key = "hello"



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
db = SQLAlchemy(app)
# db.create_all()




#User Class for DB

class User(db.Model):
	__tablename__ = 'users'
	

	_id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String, unique=True, nullable=False)
	password_hashed = db.Column(db.String(128),nullable=False)
	
from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import argon2
from sqlalchemy import create_engine, inspect


app = Flask(__name__)
app.secret_key = "hello"



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
db = SQLAlchemy(app)
# db.create_all()




#User Class for DB

class User(db.Model):
	__tablename__ = 'users'
	

	_id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String, unique=True, nullable=False)
	password_hashed = db.Column(db.String(128),nullable=False)


	def __init__(self,email:str,password_plaintext:str):
		self.email = email
		self.password_hashed = password_plaintext

	# @staticmethod
	# def _generate_password_hash(password_plaintext: str):
	# 	return argon2.hash_password(bytes(password_plaintext),bytes("salt"))
	

#Routing portion of app - 

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/login', methods=["POST","GET"])
def login():

	
	if request.method == "POST":
		email = request.form['email']
		password = request.form['password']

		

		if User.query.filter_by(email=email).first() and User.query.filter_by(password_hashed=password).first():

			return redirect(url_for("index"))

		else:
			flash("Invalid login, try again!")
			return render_template('login.html')
	
	return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
	if request.method == "POST":

		email = request.form['email']
		password = request.form['password']
		confirm_password = request.form['confirm_password']

		if password != confirm_password:
			flash('Error passwords do not match. Try again')
			return redirect(url_for("register"))
			

		existing_user  = User.query.filter_by(email=email).first()
		if existing_user:
			flash("Email already in use. Try logging in or using a different email")
			return redirect(url_for('register'))
		
		db.create_all()
		new_user = User(email=email, password_plaintext=password)
		db.session.add(new_user)
		db.session.commit()
		
		flash("Account successfully created")
		return redirect(url_for("login"))

	return render_template('register.html')


# db.create_all()
if __name__ == '__main__':
	
	app.run(debug = True)







