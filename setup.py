from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello world! <h1>YO<h1>"

if __name__ == "__main__":
	app.run()