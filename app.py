from flask import Flask, render_template, request, send_file
from image_controller import compress_image_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/image/compress', methods=['GET', 'POST'])
def image_compress():
    if request.method == 'POST':

        image_file = request.files['image']
        target_size = float(request.form['target_size'])

        compressed_image_buffer, compressed_size = compress_image_file(image_file, target_size)

        compressed_image_path = "static/compressed_image.png"
        with open(compressed_image_path, "wb") as file:
            file.write(compressed_image_buffer.getvalue())

        original_filename = os.path.splitext(image_file.filename)[0]
        optimized_filename = original_filename + "_optimized.png"

        return render_template('image_preview.html', compressed_image='compressed_image.png', compressed_size=compressed_size, optimized_filename=optimized_filename)

    return render_template('image_compression.html')

@app.route('/download/<filename>')
def download(filename):
    compressed_image_path = "static/compressed_image.png"
    return send_file(compressed_image_path, as_attachment=True, download_name=filename)

@app.route('/pdf-splitter')
def pdf_splitter():
    return render_template('pdf_splitter.html')

if __name__ == '__main__':
    app.run(debug=True)