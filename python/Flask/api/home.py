from flask import Blueprint, jsonify

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return jsonify({"message": "Unauthorized"}), 401
