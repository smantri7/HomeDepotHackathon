from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route("/")
def mainpage():
	return render_template('main.html')

if __name__ == "__main__":
    app.run()