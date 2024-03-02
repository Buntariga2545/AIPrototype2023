from crypt import methods
from doctest import debug
from flask import Flask, flash, request, redirect, render_template, make_response

import json
import sys

app = Flask(__name__)

##api
@app.route('/request',methods=['POST'])
def web_service_API():

    payload = request.data.decode("utf-8")
    imessage = json.loads(payload),

    print(imessage)
    json_data = json.dumps({'y':'received'})
    return json_data

@app.route("/")
def helloworld():
    return "<h1> Welcome to My Web Application.</h1>"

@app.route("/home", methods=['POST','GET'])
def homefn():
       return render_template("webapp1.html")

@app.route("/form", methods=['POST','GET'])
def form_info():
    if request.method == "POST":
       print('Results', file=sys.stdout)

       Agein = request.form.get('Age')
       print('Age = ', Agein, fike=sys.stdout)
       print(Agein, file=sys.stdout)
       
       weightin = request.form.get('Weight')
       print('Weight = ', weightin, file=sys.stdout)
       print(weightin, file=sys.stdout)
       return render_template("webapp.html", data = [Agein, weightin])

    elif request.method == "GET":
       print('Results', file=sys.stdout)

       Agein = request.form.get('Age')
       print('Age = ', Agein, fike=sys.stdout)
       print(Agein, file=sys.stdout)
       
       weightin = request.form.get('Weight')
       print('Weight = ', weightin, file=sys.stdout)
       print(weightin, file=sys.stdout)
       return render_template("webapp.html", data = [Agein, weightin])
       
#       print('เจอละ(POST)', file=sys.stdout)
#       Agein = request.form.get('ticketNum')
#       weightin = request.form.get('ticketNum')
#       print(Agein, file=sys.stdout)
#       print(weightin, file=sys.stdout)
#       return render_template("webapp.html", Age=Agein)











@app.route("/res", methods=['POST','GET'])
def res():
       return render_template("webapp2.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save('file')
        return render_template("webapp.html",name='upload completed')

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''   


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=5001) #host='0.0.0.0'คือสามารถให้เครื่องอื่นเห็นได้











#@app.route("/home", methods=['POST','GET'])
#def homefn():
#    if request.method == "GET":
#       print('we are in home(GET)', file=sys.stdout)
#       namein = request.args.get('fname')
#       print(namein, file=sys.stdout)
#       return render_template("webapp.html", name=namein)
#
#    elif request.method == "POST":
#        print('We are in home(POST)', file=sys.stdout)
#        namein = request.form.get('fname')
#        lastnamein = request.form.get('lname')
#        print(namein, file=sys.stdout)
#        print(lastnamein, file=sys.stdout)
#        return render_template("webapp.html",name=namein)