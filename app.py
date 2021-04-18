import os
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():

    target = os.path.join(APP_ROOT, 'gambar/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("Tampilan.html",hasil = filename)

@app.route("/upload/<filename>")
def kirim(filename):
    return send_from_directory("gambar/",filename)


if __name__ == "__main__":
    app.run()