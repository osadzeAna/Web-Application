from flask import Flask, redirect, url_for, render_template, request, session, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jerfbnje4tuef'

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dishes.sqlite'
db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    username = db.Column(db.String(80), nullable=False)

class dishes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dish_name = db.Column(db.String(30), unique=True, nullable=False)
    ingredients = db.Column(db.String(80), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/home')
def home_page():  # put application's code here
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/<name>/<int:age>')
def userage(name,age):
    return f'hi {name}, you are {age} years old!'

@app.route('/admin')
def admin():
    return redirect('/home')

@app.route('/add_dish')
def add_dish():
    if 'dish_name' in request.args:
        n = request.args['name']
        i = request.args['ingredients']
        r = request.args['rate']
        if n=='' or a=='' or r=='':
            flash('შეიტანეთ ყველა წევრი', 'error')
        elif not r.isdecimal() or r>10:
            flash('შეფასება უნდა იყოს რიცხვითი მონაცემი, მაქსიმალურია 10.')
        d1 = dishes(name=n, ingredients=i, rate=float(r))
        db.session.add(b1)
        db.session.commit()
        flash('კერძი დამატებულია', 'info')
    return render_template('add_dish.html')

@app.route('/all_dish')
def all_dish():
    return render_template('all_dish.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        p = request.form['password']
        session['username'] = user

        return redirect('/user')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'you are logged out'


if __name__ == '__main__':
    app.run(debug=True)
