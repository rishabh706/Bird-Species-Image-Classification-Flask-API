import flask
from flask import Flask,render_template,request
import tensorflow as tf
import cv2
import numpy as np
import pickle

app = Flask(__name__)

# Defing Constants
MODEL_PATH="model/model.h5"
IMAGE_SIZE=224
CHANNELS=3
NUM_IMAGES=1
RESCALE=255.

# Loading Model
loaded_model=tf.keras.models.load_model(MODEL_PATH,compile=False)

# Loading Pickle File
file=open("pickle/Bird_species.pickle","rb")
bird_species=pickle.load(file)

# Welcome Endpoint
@app.route('/',methods=['GET','POST'])
def welcome():
    response={}
    response["response"]={
            'Welcome':"Welcome to Bird Species Classification API"
        }

    return flask.jsonify(response)

def predict_image(image):
    image=cv2.imread(image)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    image=image/RESCALE
    image = np.reshape(image,[NUM_IMAGES,IMAGE_SIZE,IMAGE_SIZE,CHANNELS])
    probabilities=loaded_model.predict(image)
    prediction=np.argmax(probabilities,axis=1)
    
    for key,value in bird_species.items():
        if prediction==value:
            return key

# Prediction Endpoint
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        image_path=request.json
        image_path=image_path["image_path"]    
        prediction=predict_image(image_path)
        response={}
        response["response"]={
            'Bird Species':str(prediction)
        }
        return flask.jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

