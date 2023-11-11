from flask import Flask, render_template, request, jsonify
from bpcs.bpcs_steg_encode import encode  # Impor fungsi encoding dari modul bpcs_steg_encode
from bpcs.bpcs_steg_decode import decode  # Impor fungsi decode dari modul bpcs_steg_decode

app = Flask(__name__)

# Endpoint untuk melakukan operasi encoding
@app.route('/hide_message', methods=['POST'])
def hide_message():
    if request.method == 'POST':
        image = request.files['image']
        message = request.form['message']

        # Lakukan operasi steganografi menggunakan fungsi encode dari modul bpcs_steg_encode
        encoded_image = encode(image, message)

        # Proses operasi encoding dan kembalikan respons
        # Misalnya, mengembalikan hasil operasi encoding
        return jsonify({'result': 'Operasi encoding berhasil dilakukan'})
    
# Endpoint untuk melakukan operasi dekoding
@app.route('/extract_message', methods=['POST'])
def extract_message():
    if request.method == 'POST':
        image = request.files['image']

        # Lakukan operasi steganografi menggunakan fungsi decode dari modul bpcs_steg_decode
        extracted_message = decode(image)

        # Proses hasil dekoding dan kembalikan respons
        return jsonify({'extracted_message': extracted_message})


if __name__ == '__main__':
    app.run(debug=True)
