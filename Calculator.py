from flask import Flask, jsonify, request,send_file


app = Flask(__name__)

@app.route('/')

def hello():

    return "Hello, Server!"




if __name__ == '__main__':
    app.run(debug=True, port=3000)