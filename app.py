from flask import Flask
from flask import request
from flask import Response
from lxml import html
import requests
import json
from requests.structures import CaseInsensitiveDict
  
app = Flask(__name__)

@app.route('/https/<url>')
def root(url):    
    url = 'https://' + url
    r = requests.get(url)
    rr = Response(response=r.content, status=r.status_code)
    rr.headers["Content-Type"] = r.headers['Content-Type']
    return rr
  
@app.route('/user/<username>')
def show_user(username):
    res = {"value1":username,"value2":username,"value3":username}


    

    requests.post('https://maker.ifttt.com/trigger/wordpress/with/key/ZwaxwZ1PFl5eBknC9XGXG',data=res)
    # Greet the user
    return f'Hello {username} !'
  
# Pass the required route to the decorator.
@app.route("/hello")
def hello():

    url = "https://hf.space/embed/hnam/start/hello"
    yyy='you'
    r = requests.post(
        url,
        data=json.dumps({"input": "German:i miss {}".format(yyy)}),
        headers={"Content-Type": "application/json"},
    )

    print( r.json())
    return r.json()
    
@app.route("/")
def index():
    return "Homepage of GeeksForGeeks"
  
@app.route("/ifttt",methods=["GET"])
def ifttt():

    info = request.args.get('email') 
    pp = "DFHGKJDFG {}".format(info)
    print("DFHGKJDFG {}".format(info))
    return pp

if __name__ == "__main__":
    app.run(debug=True)