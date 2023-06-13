from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/info.html')
def about():
	return render_template('info.html')

@app.route('/home.html')
def h0me():
	return render_template('home.html')



if __name__=='__main__':
	app.run(debug=True)
