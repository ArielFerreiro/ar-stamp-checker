import os
from flask import Flask, flash, request, redirect, render_template
import predict
from PIL import Image, ImageDraw

# UPLOAD_FOLDER = '/home/victorhvivasc/mysite/static'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return "Hello, use the route /image with headers 'file':image.jpg, 'data': 'json' and method POST for predict stamp!"


@app.route('/image/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file:
            n = int(len(os.listdir('mysite/static'))/2)
            if n>10:
                lista = os.listdir('mysite/static')
                for a in lista:
                    os.remove('mysite/static/'+a)
            filename = f'mysite/static/imagen{n}.jpg'
            file.save(filename)
            p = predict.predict(filename)[0]*154
            x, y, w, h = p
            i = Image.open(filename)
            i = i.convert('RGBA')
            r = Image.new("RGBA", i.size, (0, 0, 0, 0))
            r_ = ImageDraw.Draw(r)
            r_.rectangle(((x, y), (x+w, y+h)), fill=(0, 255, 0, 128))
            img = Image.alpha_composite(i, r)
            img = img.convert("RGB")  # Remove alpha for saving in jpg format.
            img.save(f"mysite/static/imagen_pre{n}.jpg")
    return render_template("prediccion.html", prediccion=p, imagen=f'imagen_pre{n}.jpg')


if __name__ == "__main__":
    app.secret_key = "123456"
    app.run(debug=True, host="127.0.0.1", port="5000")
