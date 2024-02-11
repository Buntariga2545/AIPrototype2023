from flask import Flask, redirect, request, render_template, make_response

import json
import sys

app = Flask(__name__)

#ap1
@app.route("/home", methods=['POST','GET'])
def homefn():
    if request.method == "GET":
        print('We are in home(GET)', file=sys.stdout)
        namein = request.args.get('fname')
        print(namein, file=sys.stdout)
        return render_template("home.html",name=namein)

    elif request.method == "POST":
        print('We are in home(POST)', file=sys.stdout)
        namein = request.form.get('fname')
        lastnamein = request.form.get('lname')
        print(namein, file=sys.stdout)
        print(lastnamein, file=sys.stdout)
        return render_template("home.html",name=namein)

@app.route('/upload2', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save('file')
        return render_template("home.html",name='upload completed')


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
    app.run(host='0.0.0.0',debug=True,port=5000)#host='0.0.0.0',port=5000