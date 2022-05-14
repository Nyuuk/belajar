from flask import Blueprint, request, jsonify

auth = Blueprint('auth', __name__)
token = [311203]

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/signup')
def signup():
    return "SignUp"

@auth.route('/logout')
def logout():
    return 'LogOut'

@auth.route('/api')
def api():
    return "This api BVVIP", 200

