from . import auth_bp
from flask import render_template, request, redirect, flash
from app.models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

@auth_bp.route('/login')
def show_index():
    return render_template('auth/login.html')

@auth_bp.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect('/auth/login')
    return redirect('/admin/')

@auth_bp.route('/signup')
def show_signup():
    return render_template('auth/signup.html')

@auth_bp.route('/signup', methods=['POST'])
def signup_post():
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return redirect('/auth/signup')
    
    new_user = User(
        email=email,
        username=username,
        password=generate_password_hash(password, method='scrypt')
    )
    db.session.add(new_user)
    db.session.commit()
    return redirect('/auth/login')