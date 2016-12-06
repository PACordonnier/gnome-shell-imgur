import os
from flask import Flask, request, jsonify, redirect, url_for, send_from_directory
from werkzeug import secure_filename

UPLOAD_FOLDER = '/tmp/uploads'
SERVER_URL = 'YOUR URL'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
data = { 'data': {
        'link': ''}    
    }
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/image", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            data['data']['link'] = SERVER_URL + filename
            return jsonify(**data)
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    <p>%s</p>
    """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],))

@app.route("/get/<path:path>")
def get(path):
    return send_from_directory(UPLOAD_FOLDER, path)

if __name__ == "__main__":
	app.run()
