from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

from.index import index_views
from App.models import Staff, Student, User
from App.controllers import (
    create_user,
    jwt_authenticate,
    login 
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

'''
Page/Action Routes
'''

@auth_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)


@auth_views.route('/identify', methods=['GET'])
@login_required
def identify_page():
    return jsonify({'message': f"username: {current_user.username}, id : {current_user.id}"})


@auth_views.route('/login', methods=['POST'])
def login_action():
    data = request.form
    user = login(data['username'], data['password'])
    if user:
        user_type = type(user)
        print("User type:", user_type)
        login_user(user)
        if (user.user_type == "staff"):
            return redirect("/staff_dashboard")  # Redirect to student dashboard
        elif (user.user_type == "student"):
            return redirect("/student_dashboard")  # Redirect to staff dashboard
        # return redirect("/test")
        return 'cannot find type', 401
    return 'bad username or password given', 401

@auth_views.route('/student_dashboard', methods=['GET'])
def student_home_page():
    return render_template('Student-Home.html')

@auth_views.route('/staff_dashboard', methods=['GET'])
def staff_home_page():
    return render_template('Staff-Home.html')

@auth_views.route('/logout', methods=['GET'])
def logout_action():
    logout_user()
    flash('You are now logged out.')
    return render_template('login.html')

'''
API Routes
'''

# @auth_views.route('/api/users', methods=['GET'])
# def get_users_action():
#     users = get_all_users_json()
#     return jsonify(users)

# @auth_views.route('/api/users', methods=['POST'])
# def create_user_endpoint():
#     data = request.json
#     create_user(data['username'], data['password'])
#     return jsonify({'message': f"user {data['username']} created"})

# @auth_views.route('/api/login', methods=['POST'])
# def user_login_api():
#   data = request.json
#   token = jwt_authenticate(data['username'], data['password'])
#   if not token:
#     return jsonify(message='bad username or password given'), 401
#   return jsonify(access_token=token)

# @auth_views.route('/api/identify', methods=['GET'])
# @jwt_required()
# def identify_user_action():
#     return jsonify({'message': f"username: {jwt_current_user.username}, id : {jwt_current_user.id}"})