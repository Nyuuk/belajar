from flask import Blueprint, jsonify, request
from .__func import auth as get_auth_token

app = Blueprint('post', __name__)

# New user Tele
@app.route('/api/post/telegram', methods=['POST'])
def new_user_tele():
    from .__telegram import new_user
    headers = request.headers
    args = request.args
    if not get_auth_token(headers):
        return jsonify({"message": "Unauthorized"}), 401
    if 'user_id' not in args or 'username' not in args:
        return jsonify({
            "message": "Authorized",
            "data": "user_id or username not defined"}), 404
    if 'saldo' not in args:
        saldo = 0
    else:
        saldo = args['saldo']
    if 'status' not in args:
        status = "user"
    else:
        status = args['status']
    format_js = {"user_id": int(args['user_id']), "username": args['username'], "saldo": saldo, "status": status}
    req = new_user(format_js)
    if not req['status']:
        return jsonify({
            "message": "Authorized",
            "data": req['message']}), 404
    return jsonify({
        "message": "Authorized",
        "data": req}), 200

@app.route('/api/post/telegram/req-saldo', methods=['POST'])
def req_add_saldo():
    from .__telegram import req_saldo
    headers = request.headers
    args = request.get_json()
    if not get_auth_token(headers):
        return jsonify({"message": "Unauthorized"}), 401
    if 'user_id' not in args or 'saldo' not in args:
        return jsonify({
            "message": "Authorized",
            "data": "user_id or saldo not defined"}), 404
    if not args['saldo'].isdigit():
        return jsonify({
            "message": "Authorized",
            "data": "saldo not is digit"}), 404
    val = {"meth": "add", "user_id": args['user_id'], "saldo": args['saldo']}
    req = req_saldo(val)
    if not req['status']:
        return jsonify({
            "message": "Authorized",
            "data": req['message']}), 404
    return jsonify({
        "message": "Authorized",
        "data": req}), 200

@app.route('/api/post/vpnremote', methods=['POST'])
def add_uss_vpnremote():
    """
    {'created_by': ['user-telegram/user-web-dll',
    id_user],
    'perpanjang': True/False,
    'uss_vpn': 'uss_vpn',
    'pw_vpn': 'pw_vpn',
    'fwd_1': portlocal, 'fwd_2': portlocal, 'fwd_3': portlocal,
    'exp': 'YYYY-MM-DD H:M'}
    """
    from .__vpn_remote import add_uss as vpnremote_add
    headers = request.headers
    args = request.get_json()
    if not get_auth_token(headers):
        return jsonify({"message": "Unauthorized"}), 401
    if 'created_by' not in args:
        return jsonify({"message": "Authorized", "data": "created_by not defined"}), 404
    if 'uss_vpn' not in args:
        return jsonify({"message": "Authorized", "data": "uss_vpn not defined"}), 404
    if 'perpanjang' not in args:
        return jsonify({"message": "Authorized", "data": "perpanjang not defined"}), 404
    if 'pw_vpn' not in args:
        return jsonify({"message": "Authorized", "data": "pw_vpn not defined"}), 404
    if 'fwd_1' not in args and 'fwd_2' not in args and 'fwd_3' not in args:
        return jsonify({"message": "Authorized", "data": "fwd_1, fwd_2, fwd_3 not defined"}), 404
    if 'exp' not in args:
        return jsonify({"message": "Authorized", "data": "exp not defined"}), 404
    req = vpnremote_add(args)
    if req['status'] == False:
        return jsonify({"message": "Authorized", "data": req['message']}), 404
    else:
        return jsonify({"message": "Authorized", "data": req['message']}), 200
