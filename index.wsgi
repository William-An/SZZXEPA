# encoding=utf8
import sae

from bottle import Bottle,route, run, template, request, response,  post, get, static_file,debug
app=Bottle()
debug(True) 

@app.get('/')
def web_index():
    return template("index")

application = sae.create_wsgi_app(app)