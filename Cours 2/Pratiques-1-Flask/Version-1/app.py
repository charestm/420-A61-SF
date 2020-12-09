from flask import Flask,render_template,url_for,request,jsonify

app = Flask(__name__)

# ML Pkgs

# Load Models

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/predict',methods=['GET','POST'])
def predict():
	# Receives the input query from form
	

	return render_template("index.html")



if __name__ == '__main__':
	app.run(debug=True)