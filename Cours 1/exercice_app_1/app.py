# Load Core Pkgs

from flask import Flask,render_template

# Init App
app = Flask(__name__)

@app.route('/')
def index():
	return "Hello 420-A61-SF "

# To Listen on Local Host
if __name__ == '__main__':
	app.run(debug=True)