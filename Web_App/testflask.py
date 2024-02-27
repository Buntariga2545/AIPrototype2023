from crypt import methods
from doctest import debug
from flask import Flask, flash,request, redirect, render_template, make_response

import json
import sys

app = Flask(__name__)
##model = pickle.load(open('model.pk', 'rb'))


##api
@app.route("/")
def helloworld():
    return "Hello, World!"

@app.route("/name")
def hellodew():
    return "Hello, Dew!"

@app.route("/home2")
def home2():
    return render_template("webapp.html",name='dew')

@app.route('/')
def main():
    return render_template("webapp.html")

@app.route('/predict', methods = ['POST'])
def getPredict():



@app.route("/home", methods=['POST','GET'])
def homefn():
    return render_template("webapp1.html")

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
    
@app.route("/form", methods=['POST','GET'])
def form_info():
    if request.method == "GET":
       print('เจอละ(GET)', file=sys.stdout)

       Agein = request.args.get('ticketNum')
       print(Agein, file=sys.stdout)
       return render_template("webapp.html", Age=Agein)

    elif request.method == "POST":
       print('เจอละ(POST)', file=sys.stdout)
       Agein = request.form.get('ticketNum')
       weightin = request.form.get('ticketNum')
       print(Agein, file=sys.stdout)
       print(weightin, file=sys.stdout)
       return render_template("webapp.html", Age=Agein)


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
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0',port=5001