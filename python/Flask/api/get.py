from flask import Blueprint, jsonify, request
from .__func import auth as get_auth_token
from .__func import get_name_token
geta = Blueprint('get', __name__)

@geta.route('/api/get', methods=['GET'])
def api_get():
    headers = request.headers
    if not get_auth_token(headers):
        return jsonify({"message": "Unauthorized"}), 401
    args = request.args
    return jsonify({"message": "Authorized",
                    "data": args,
                    "token-name": get_name_token(headers)
                    }), 200

#list User telegram bot
@geta.route('/api/get/telegram', methods=['GET'])
def get_list_user():
    from .__telegram import get_user
    args = request.get_json()
    headers = request.headers
    if not get_auth_token(headers):
        return jsonify({"message": "Unauthorized"}), 401
    if 'user_id' not in args:
        uss_id = None
    else:
        uss_id = args['user_id']
    return jsonify({
        "message": "Authorized",
        "data": get_user(args['meth'], uss_id)
        }), 200

@geta.route('/api/get/telegram/req-saldo', methods=['GET'])
def get_req_saldo():
    from .__telegram import get_req_saldo
    args = request.get_json()
    headers = request.headers
    if not get_auth_token(headers):
        return jsonify({"message": "Unauthorized"}), 401
    if 'meth' not in args:
        return jsonify({
            "message": "Authorized",
            "data": "meth not defined"}), 404
    if 'user_id' not in args:
        uss_id = None
    else:
        uss_id = args['user_id']
    return jsonify({"message": "Authorized",
                    "data": get_req_saldo(args['meth'], uss_id)
                    }), 200
