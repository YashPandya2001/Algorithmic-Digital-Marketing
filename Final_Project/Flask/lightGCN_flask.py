from flask import Flask
from flask import request,redirect,render_template,session
import requests
import base64
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def iIndex():
    return render_template('index.html')

@app.route('/About.html')
def about():
    return render_template('About.html')

@app.route('/Menu.html')
def menu():
    return render_template('Menu.html')

@app.route('/Contact.html')
def contact():
    return render_template('Contact.html')

@app.route('/home.html', methods=["GET", "POST"])
def index():
    return render_template("home.html")


@app.route('/pipe', methods=["GET", "POST"])
def pipe():

    UserId = request.form.get("UserId")
    ItemId =  request.form.get("ItemId")

    import requests
    url = "http://localhost:8000/recommendation?userId={}&itemID={}".format(UserId,ItemId)
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))

    return response.json()


if __name__ == "__main__":
    app.run(debug=True, port=5000)