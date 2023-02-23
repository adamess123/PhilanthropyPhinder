from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, mail, app
from flask_mail import Message
from flask_login import login_user, login_required, logout_user, current_user
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

s=Serializer('secret', 30)
token=s.dumps({'id'}).decode('utf-8')
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.index'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 3:
            flash('Email must be greater than 2 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created.', category='success')
            return redirect(url_for('views.index'))

    return render_template("register.html", user=current_user)

def reset_pass_info(user):
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')
    new_password2 = request.form.get('new_password2')

    if user:
        if old_password != User.password:
            flash('Old password incorrect!')
        elif new_password != new_password2:
            flash('New passwords must match!')
        else:
            User.password = generate_password_hash(new_password, method='sha256')
            flash('Password successfully changed.')
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token.html', token=token, _external=True)}
    
If you did not request to reset your password, then you may ignore this email.
'''
    mail.send(msg)
@auth.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    if current_user.is_authenticated:
        return redirect(url_for('index.html'))
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('login.html'))

    return render_template("password_reset.html", user=current_user)


@auth.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('index.html'))
    user = User.verify_reset_token(token)
    if User is None:
        flash('Token is invalid or expired.', 'warning')
        return redirect(url_for('password_reset.html'))
    reset_pass_info(user)
    db.session.commit()
    flash('Your password has been updated! You can now log in.')
    return render_template("reset_token.html", user=current_user)
