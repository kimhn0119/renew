from flask import Flask
import requests
  
app = Flask(__name__)
  
@app.route('/user/<username>')
def show_user(username):
    res = {"value1":username,"value2":username,"value3":username}


    

    #requests.post('https://maker.ifttt.com/trigger/wordpress/with/key/ZwaxwZ1PFl5eBknC9XGXG',data=res)
    # Greet the user
    return f'Hello {username} !'
  
# Pass the required route to the decorator.
@app.route("/hello")
def hello():
    return "Hello, Welcome to GeeksForGeeks"
    
@app.route("/")
def index():
    return "Homepage of GeeksForGeeks"
  
if __name__ == "__main__":
    app.run(debug=True)