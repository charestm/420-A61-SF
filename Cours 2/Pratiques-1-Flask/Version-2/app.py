from flask import Flask,render_template,url_for,request,jsonify
# ML Pkgs
import numpy as np

import pandas as pd 

# ML Pkgs
import os
#import joblib
app = Flask(__name__)


# Load Models

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/dataset')
def dataset():
	df = pd.read_csv("data/clean_dataset.csv")
	return render_template("dataset.html",df_table=df)


@app.route('/predict',methods=['GET','POST'])
def predict():
	# Receives the input query from form
	

	return render_template("index.html")



if __name__ == '__main__':
	app.run(debug=True)