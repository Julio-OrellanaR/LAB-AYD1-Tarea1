from flask import Flask, jsonify, render_template, request,send_file
from Crypto.Cipher import AES  #Works

app = Flask(__name__, template_folder='plantillas')

@app.route('/', methods = ["GET"])

def formulario():
    
    data = "<br /> <b>Nombre:</b> Julio José Orellna Ruíz  <br /><br /> <b> Carnet:</b> 201908120"

    return data


if __name__ == '__main__':
    app.run(debug=True, port=4000)