from flask import Blueprint, jsonify, request
from .__func import auth as get_auth_token

app = Blueprint('put', __name__)

@app.route('/api/put/telegram', methods=['PUT'])
def update_user():
    from .__telegram import update_user
    headers = request.headers
    args = request.get_json()
    if not get_auth_token(headers):
        return jsonify({"message": "Unauthorized"}), 401
    if 'user_id' not in args or 'username' not in args:
        return jsonify({
            "message": "Authorized",
            "data": "user_id or username not defined"}), 404
    val = {'user_id': args['user_id'], "username": args['username']}
    req = update_user(val)
    if not req['status']:
        return jsonify({
            "message": "Authorized",
            "data": req['message']}), 404
    return jsonify({
        "message": "Authorized",
        "data": req}), 200

@app.route('/api/put/telegram/saldo', methods=['PUT'])
def put_saldo():
    from .__telegram import mod_saldo
    headers = request.headers
    args = request.get_json()
    if not get_auth_token(headers):
        return jsonify({"message": "Unauthorized"}), 401
    if 'user_id' not in args or 'saldo_new' not in args:
        return jsonify({
            "message": "Authorized",
            "data": "user_id or saldo_new not defined"}), 404
    if not args['saldo_new'].isdigit():
        return jsonify({
            "message": "Authorized",
            "data": "saldo_new not is digit"}), 404
    req = mod_saldo(args['user_id'], args['saldo_new'])
    if not req['status']:
        return jsonify({
            "message": "Authorized",
            "data": req['message']}), 404
    return jsonify({
        "message": "Authorized",
        "data": req}), 200

@app.route('/api/put/vpnremote', methods=['PUT'])
def put_vpnremote():
    from .__vpn_remote import mod_uss as vpnremote_mod_uss
    headers = request.headers
    args = request.get_json()
    if not get_auth_token(headers):
        return jsonify({"message": "Unauthorized"}), 401
    if 'uss_vpn' not in args:
        return jsonify({"message": "Authorized", "data": "uss_vpn not defined"})
    req = vpnremote_mod_uss(args)
    if not req['status']:
        return jsonify({"message": "Authorized", "data": req['message']}), 404
    return jsonify({"message": "Authorized", "data": req['message']}), 200
