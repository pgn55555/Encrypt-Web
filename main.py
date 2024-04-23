from flask import Flask, render_template, send_file, request

import os

from src.main import Main

app = Flask(__name__)
app.secret_key = "ItIsASecret"

def delete_files() -> None:
    for filename in os.listdir("files"):
        file_path = os.path.join("files", filename)
        os.remove(file_path)

@app.route("/")
def encrypt():
    delete_files()
    return render_template('encrypt.html')

@app.route("/decrypt")
def decrypt():
     delete_files()
     return render_template('decrypt.html')

@app.route("/hackermode")
def hackermode():
     delete_files()
     return render_template('hackermode.html')

@app.route('/submit_encrypt', methods=['POST'])
def submit_encrypt():
    uploaded_file = request.files['fileInput']
    file_path = os.path.join("files", uploaded_file.filename)
    uploaded_file.save(file_path)

    algo = request.form['selectAlgo']
    key = request.form['keyAlgo']
    if key == "":
        key = "generate"

    program = Main([file_path, algo, 'encrypt', key])
    program.start()
    
    return send_file(file_path, as_attachment=True)

@app.route('/submit_decrypt', methods=['POST'])
def submit_decrypt():
    uploaded_file = request.files['fileInput']
    file_path = os.path.join("files", uploaded_file.filename)
    uploaded_file.save(file_path)

    algo = request.form['selectAlgo']
    key = request.form['keyAlgo']

    program = Main([file_path, algo, 'decrypt', key])
    program.start()

    return send_file(file_path, as_attachment=True)

@app.route('/submit_hackermode', methods=['POST'])
def submit_hackermode():
    uploaded_file = request.files['fileInput']
    file_path = os.path.join("files", uploaded_file.filename)
    uploaded_file.save(file_path)

    program = Main([file_path, 'caesar', 'decrypt', 'hackermode'])
    program.start()
    
    return send_file(file_path, as_attachment=True)
