from PyPDF2 import PdfReader
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	reader = PdfReader("Lindani Pani CV - October_2022.pdf")
	text = ""
	for page in reader.pages:
		text += page.extract_text() + "\n"
	print(text.split('\n'))
	# pdfFileObj.close() 
	

	return render_template('home.html')


if __name__ == "__main__":
	# Used when running locally only. When deploying to Google App
	# Engine, a webserver process such as Gunicorn will serve the app. This
	# can be configured by adding an `entrypoint` to app.yaml.
	app.run(debug=True)