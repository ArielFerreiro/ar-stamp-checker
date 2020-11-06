from keras.models import load_model
from PIL import Image
import numpy as np


def predict(path):
    model = load_model("modelo/deteccion_etiquetas_box_1.h5")
    img = Image.open(path)
    img.resize((224, 224))
    img = np.expand_dims(img, axis=0)
    pre = model.predict(img/255)
    return pre
