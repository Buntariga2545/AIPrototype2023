from crypt import methods
from doctest import debug
from flask import Flask, flash, request, redirect, render_template, make_response
from joblib import dump, load

import numpy as np
import pandas as pd
import joblib 
import pickle
import json
import sys

with open(f'model/model.pkl', 'rb') as f:
    model = load(f)

app = Flask(__name__)

#load the model
#model = pickle.load(open('savemodel.sav', 'rb'))

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
#       print('เจอละ(POST)', file=sys.stdout)
#       Agein = request.form.get('ticketNum')
#       weightin = request.form.get('ticketNum')
#       print(Agein, file=sys.stdout)
#       print(weightin, file=sys.stdout)
#       return render_template("webapp.html", Age=Agein)
    if flask.request.method == 'POST':
        Genderin = flask.request.form['Gender']
        Agein = flask.request.form['Age']
        weightin = flask.request.form['Weight']
        heightin = flask.request.form['Height']
        BMIin = flask.request.form['BMI']
        Tempin = flask.request.form['Temp']
        RHin = flask.request.form['RH']
        Vin = flask.request.form['V']
        TMRTin = flask.request.form['TMRT']
        areain = flask.request.form['area']

        input_variables = pd.DataFrame([[Genderin, Agein, weightin, heightin, BMIin, Tempin, RHin, Vin, TMRTin, areain]],
                                       columns=['Gender', 'Age', 'Weight', 'Height', 'BMI',
                                                'Temp', 'RH', 'V', 'TMRT', 'area'],
                                       dtype='float',
                                       index=['input'])

        predictions = model.predict(input_variables)[0]
        print(predictions)

#        return flask.render_template('webapp2.html', original_input={'Gender': Genderin, 'Age': Agein, 'Weight': weightin, 
#                                                                     'Height': heightin, 'BMI': BMIin, 'Temp': Tempin, 
#                                                                     'RH': RHin, 'V': Vin, 'TMRT': TMRTin, 
#                                                                     'area': areain},
#                                     result=predictions)
    
        return render_template("webapp2.html", prediction=predictions)


#        try:
#            prediction = preprocessDataAndPredict(Age, Weight, Height, BMI, Temp, RH, V, MRT)
            # Pass prediction to template
#            return render_template('webapp2.html', prediction=prediction)
#        except ValueError:
#            return "Please Enter valid values"
#    else:
        # Handle GET request
#        return render_template('webapp2.html')

#def preprocessDataAndPredict(Age, Weight, Height, BMI, Temp, RH, V, MRT):
    # Put all inputs in array
#    test_data = np.array([[Age, Weight, Height, BMI, Temp, RH, V, MRT]])
    
    # Open file
#    file = open("model.pk","rb")
    # Load trained model
#    trained_model = joblib.load(file)
    # Predict
#    prediction = trained_model.predict(test_data)
    
#    return prediction
    
#def preprocessDataAndPredict(Age, Weight, Height, BMI, Temp, RH, V, MRT):
    #put all inputs in array
#    test_data = pd.read_csv('test_data.csv')
#    print(test_data)
    #open file
#    file = open("model.pk","rb")
    #load trained model
#    trained_model = joblib.load(file)
    #predict
#    prediction = trained_model.predict(test_data)
#    return render_template('webapp2.html', prediction = prediction)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save('file')
        return render_template("webapp.html", name='upload completed')

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