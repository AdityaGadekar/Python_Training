# gwt post patch
from flask import  Flask, request
app = Flask(__name__)
@app.route("/")
def index():
    return '<h1> Hello world. We are using Flask</h1>'

#Dyanamic routing
#http:127.0.0.1/Aditya

@app.route('/user/<name>')
def user(name):
    return '<h1> Hello, World, %s!<h1>' %name

#headers
@app.route("/headers")
def headers():
    user_agent= request.headers.get('User-Agent')
    return '<p> Your Browser is,%s <p>' %user_agent







if __name__=='__main__':
    app.run(debug=True)