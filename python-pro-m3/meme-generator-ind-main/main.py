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
        text_top = request.form.get("textTop")
        text_bottom = request.form.get("textBottom")

        # Tugas #3. Menerima posisi teks
        text_top_y = request.form.get("textTop_y")
        text_bottom_y = request.form.get("textBottom_y")
        selected_color = request.form.get("color-selector")
       

        # Tugas #3. Menerima warna teks
        

        return render_template('index.html', 
                               # Menampilkan gambar yang dipilih
                               selected_image=selected_image, 

                               # Tugas #2. Menampilkan teks
                               text_top=text_top,
                               text_bottom=text_bottom,
                
                               # Tugas #3. Menampilkan warna
                               selected_color = selected_color,
                               
                               # Tugas #3. Menampilkan posisi teks
                               text_top_y = text_top_y,
                               text_bottom_y = text_bottom_y


                               )
    else:
        # Menampilkan gambar pertama secara default
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
