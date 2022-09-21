from flask import Flask
from flask import request
import requests
from requests.structures import CaseInsensitiveDict
  
app = Flask(__name__)
  
@app.route('/user/<username>')
def show_user(username):
    res = {"value1":username,"value2":username,"value3":username}


    

    requests.post('https://maker.ifttt.com/trigger/wordpress/with/key/ZwaxwZ1PFl5eBknC9XGXG',data=res)
    # Greet the user
    return f'Hello {username} !'
  
# Pass the required route to the decorator.
@app.route("/hello")
def hello():
#https://hf.space/embed/hnam/start/infer_t5?input=German:%20There%20are%20many%20ducksdfgdfgdfg


    url = "https://hf.space/embed/hnam/start/hello"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = """
    {"input":"fdgdf"}

    """


    resp = requests.post(url, headers=headers, data=data)

   

    print(resp)
    return "Hello, Welcome to GeeksForGeeks".resp
    
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