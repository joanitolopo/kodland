# Impor
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Hasil formulir
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # mendapatkan gambar yang dipilih
        selected_image = request.form.get('image-selector')

        # Tugas #2. Menerima teks
        

        # Tugas #3. Menerima posisi teks
       

        # Tugas #3. Menerima warna teks
        

        return render_template('index.html', 
                               # Menampilkan gambar yang dipilih
                               selected_image=selected_image, 

                               # Tugas #2. Menampilkan teks
                               

                               # Tugas #3. Menampilkan warna
                               
                               
                               # Tugas #3. Menampilkan posisi teks

                               )
    else:
        # Menampilkan gambar pertama secara default
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
