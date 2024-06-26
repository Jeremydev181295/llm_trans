from flask import Flask, request, render_template
import os
from werkzeug.utils import secure_filename
import llm_translator_final

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result_filename = llm_translator_final.main(filename)
            return "<a href=http://127.0.0.1:8081/>" + result_filename + "</a>"
    return render_template('upload.html')


if __name__ == '__main__':
    from waitress import serve
    
    serve(app, host='127.0.0.1', port=8081)
