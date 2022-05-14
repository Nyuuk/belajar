from flask import Blueprint, jsonify, request
from .__func import auth as get_auth_token

app = Blueprint('delete', __name__)

@app.route('/api/delete/telegram/req-saldo', methods=['DELETE'])
def del_req_saldo():
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
    val = {"meth": "del", "user_id": args['user_id'], "saldo": args['saldo']}
    req = req_saldo(val)
    if not req['status']:
        return jsonify({
            "message": "Authorized",
            "data": req['message']}), 404
    return jsonify({
        "message": "Authorized",
        "data": req}), 200

@app.route('/api/delete/vpnremote', methods=['DELETE'])
def del_uss_vpnremote():
    from .__vpn_remote import del_uss as vpnremote_del_uss
    headers = request.headers
    args = request.get_json()
    if not get_auth_token(headers):
        return jsonify({"message": "Unauthorized"}), 401
    if 'uss_vpn' not in args:
        return jsonify({
            "message": "Authorized",
            "data": "uss_vpn not defined"})
    req = vpnremote_del_uss(args)
    if not req['status']:
        return jsonify({
            "message": "Authorized",
            "data": req['message']}), 404
    return jsonify({
        "message": "Authorized",
        "data": req}), 200
