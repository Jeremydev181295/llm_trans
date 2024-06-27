from flask import Flask, request, render_template, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename
import llm_translator

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

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
            result_filename = llm_translator.trans(filename)
            # result_file_path = os.path.join(app.config['RESULT_FOLDER'], result_filename)
            # result_url = url_for('static', filename=result_file_path)
            # return f"<a href='{result_url}'>{result_filename}</a>"

            directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), app.config['RESULT_FOLDER'])
            return send_from_directory(directory, result_filename)
            # return {"directory":directory, "filename": result_filename}
    # return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
