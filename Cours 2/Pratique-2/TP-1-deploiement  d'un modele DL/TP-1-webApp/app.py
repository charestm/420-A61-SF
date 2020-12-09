import os
import sys

# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# TensorFlow et tf.keras
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Quelques utilitaires
import numpy as np
from util import base64_to_pil


# Déclarez une application flask 
app = Flask(__name__)


# Vous pouvez utiliser un modèle pré-formé de Keras
# Check https://keras.io/applications/
from keras.applications.mobilenet_v2 import MobileNetV2
model = MobileNetV2(weights='imagenet')

print('Modèle chargé. Vérifiez http://127.0.0.1:5000/')


# Modèle enregistré avec Keras model.save ()
MODEL_PATH = 'models/your_model.h5'

# Chargez votre propre modèle formé
# model = load_model(MODEL_PATH)
# model._make_predict_function()          # Nécessaire
# print('Modèle chargé. Commencez à servir ...')


def model_predict(img, model):
    img = img.resize((224, 224))

    # Prétraitement de l'image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    # Faites attention à la façon dont votre modèle formé gère les entrées
    # sinon, il ne fera pas de prédiction correcte!
    x = preprocess_input(x, mode='tf')

    preds = model.predict(x)
    return preds


@app.route('/', methods=['GET'])
def index():
    # Page d'accueil
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Obtenez l'image par request post 
        img = base64_to_pil(request.json)

        # Enregistrez l'image dans ./uploads
        # img.save("./uploads/image.png")

        # Faire des prédictions
        preds = model_predict(img, model)

        # Traitez votre résultat pour l'homme
        pred_proba = "{:.3f}".format(np.amax(preds))    # Max probability
        pred_class = decode_predictions(preds, top=1)   # ImageNet Decode

        result = str(pred_class[0][0][1])               # Convertir en chaîne
        result = result.replace('_', ' ').capitalize()
        
        # Sérialiser le résultat, vous pouvez ajouter des champs supplémentaires
        return jsonify(result=result, probability=pred_proba)

    return None


if __name__ == '__main__':
    # app.run(port=5002, threaded=False)

    # Servir l'application avec gevent
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
