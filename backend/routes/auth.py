# from flask import Blueprint, render_template, redirect, url_for, request, flash
# # from werkzeug.security import generate_password_hash, check_password_hash
# # from flask_login import login_user, logout_user, login_required
# # from backend.models.user import db, User

# def home():
#     return render_template('home.home')
# # auth_bp = Blueprint('auth', __name__)

# # @auth_bp.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         # username = request.form.get('username')
# #         # password = request.form.get('password')

# #         user = User.query.filter_by(username=username).first()
# #         if user and check_password_hash(user.password, password):
# #             login_user(user)
# #             return redirect(url_for('home.home'))
# #         else:
# #             flash('Invalid username or password')

# #     return render_template('login.html')

# # @auth_bp.route('/signup', methods=['GET', 'POST'])
# # def signup():
# #     if request.method == 'POST':
# #         username = request.form.get('username')
# #         password = request.form.get('password')

# #         existing_user = User.query.filter_by(username=username).first()
# #         if existing_user:
# #             flash('Username already exists')
# #             return redirect(url_for('auth.signup'))

# #         new_user = User(username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))
# #         db.session.add(new_user)
# #         db.session.commit()
# #         login_user(new_user)
# #         return redirect(url_for('home'))

# #     return render_template('signup.html')

# # @auth_bp.route('/logout')

# # def logout():
# #     logout_user()
# #     return redirect(url_for('auth.login'))


from flask import render_template

# This file is no longer used since authentication is not required.
# You can delete it or keep it as a placeholder for future use.

def home():
    return render_template('home.home')