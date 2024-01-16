from flask import Flask, redirect, request, render_template, make_response

import json
import sys

app = Flask(__name__)

#ap1
@app.route("/request", methods=['POST'])
def web_service_API():

    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload)

    print(inmessage)

    json_data = json.dumps({'y': 'received!'})
    return json_data

@app.route("/")
def helloworld():
    return "Hello, World!"

@app.route("/name")
def hellodew():
    return "Hello, Dew!"

@app.route("/home2")
def home2():
    return render_template("home.html",name='dew')

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

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save('file')
        return render_template("home.html",name='upload completed')
        # check if the post request has the file part
        # if 'file' not in request.files:
        #     flash('No file part')
        #    return redirect(request.url)
    
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)

        #return redirect(url_for('homefn', name='upload completed'))

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