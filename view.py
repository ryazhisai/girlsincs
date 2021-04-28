# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template

#create a Flask instance
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("map.html")

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port='8080')