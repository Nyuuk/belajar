from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config["debug"] = True

@app.route('/', methods=['GET'])
def hello():
    data = [{
        'nama': 'Adnan',
        'pekerjaan': 'pelajar',
        'pesan': 'Hello world'
        }]
    return make_response(jsonify({'data': data}), 200)

app.run()
