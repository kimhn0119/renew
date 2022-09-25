from flask import Flask
from flask import request
from flask import Response
from lxml import html
import requests
import json
from requests.structures import CaseInsensitiveDict
import wikipediaapi

   

  
app = Flask(__name__)



@app.route('/https/<url>')
def root2(url):    
    url = 'https://' + url

    
    r = requests.get(url)
    rr = Response(response=r.content, status=r.status_code)
    rr.headers["Content-Type"] = r.headers['Content-Type']
    return rr
@app.route('/wiki/<mystring>')
def wiki(mystring):   

    def print_sections(sections, level=0):
        sections2 = ''

        for s in sections:
            sections2 = sections2 +   ' ||| '+ s.title
            #print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:40]))
            #print_sections(s.sections, level + 1)
        return sections2    

    def print_categories(page):

        rt = ''
        categories = page.categories
        for title in sorted(categories.keys()):
            rt = rt + ' ||| '+  title
            #print("%s: %s" % (title, categories[title]))
        return rt 
   # url = 'https://' + url

    wiki_wiki = wikipediaapi.Wikipedia(
         language='en',
         extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    cat =  wiki_wiki.page(mystring).categorymembers
    elasticdoc =[]

    for c in cat.values():
        print(index,"%s: %s (nss: %d)" % ("*" * (1 + 1), c.title, c.ns))
        if  c.ns == 0:

            cccttt= ''
           # cccttt= print_categories(c)
            
            sections= ''
            #sections= print_sections(c.sections)
            links= ''

            elasticdoc.append([c.title,c.fullurl,c.text,cccttt,sections,links])



    json_string = json.dumps(elasticdoc)

   # json_string = json.dumps(r)

    print( json_string)
    return json_string


    # r = requests.get(url)
    # rr = Response(response=r.content, status=r.status_code)
    # rr.headers["Content-Type"] = r.headers['Content-Type']
   # return rr
  
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