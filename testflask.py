from crypt import methods
from doctest import debug
from flask import Flask, flash, request, redirect, render_template, make_response
from joblib import dump, load
from sklearn.preprocessing import StandardScaler

import numpy as np
import pandas as pd
import joblib 
import pickle
import json
import sys


app = Flask(__name__)

#with open(f'../AIPrototype2023/model/model.pkl', 'rb') as f:
#    model = load(f)
with (open(f'../AIPrototype2023/model/tamodel.pkl', 'rb')) as f:
    tamodel = load(f)
with (open(f'../AIPrototype2023/model/tsvmodel.pkl', 'rb')) as f:
    tsvmodel = load(f)


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
    if request.method == "GET":
        return render_template("webapp.html")
    
    elif request.method == "POST":
        Genderin = int(request.form.get('Gender'))
        print('Gender = ', Genderin, file=sys.stdout)
        Agein = int(request.form.get('Age'))
        print('Age = ', Agein, file=sys.stdout)      
        Weightin = float(request.form.get('Weight')) 
        print('Weight = ', Weightin, file=sys.stdout)
        Heightin = int(request.form.get('Height'))
        print('Height = ', Heightin, file=sys.stdout)
        Tempin = float(request.form.get('Temp'))
        print('Temp = ', Tempin, file=sys.stdout)
        RHin = float(request.form.get('RH'))
        print('RH = ', RHin, file=sys.stdout)
        Vin = float(request.form.get('V'))
        print('V = ', Vin, file=sys.stdout)
        TMRTin = float(request.form.get('TMRT'))
        print('TMRT = ', TMRTin, file=sys.stdout)
        Areain = int(request.form.get('Area'))
        print('Area = ', Areain, file=sys.stdout)
        Seasonsin = int(request.form.get('Seasons'))
        print('Seasons = ', Seasonsin, file=sys.stdout)


        try:
            prediction1 = preprocessDataAndPredict_TA(Genderin, Agein, Weightin, Heightin, Tempin, RHin, Vin, TMRTin, Areain, Seasonsin)
            prediction2 = preprocessDataAndPredict_TSV(Genderin, Agein, Weightin, Heightin, Tempin, RHin, Vin, TMRTin, Areain, Seasonsin)           
            # Pass predictions to template
            return render_template('webapp2.html', prediction1=prediction1, prediction2=prediction2)
        
        except ValueError:
            return "Please Enter valid values"


def preprocessDataAndPredict_TA(Genderin, Agein, Weightin, Heightin, Tempin, RHin, Vin, TMRTin, Areain, Seasonsin):
    test_data1 = [[Genderin, Agein, Weightin, Heightin, Tempin, RHin, Vin, TMRTin, Areain, Seasonsin]]


    test_data1 = np.array(test_data1)
    test_data1 = pd.DataFrame(test_data1)
    print(test_data1)
    #scaling data
    scaler = StandardScaler()
    test_data_scaled1 = scaler.fit_transform(test_data1)

    #predict
    prediction1 = tamodel.predict(test_data_scaled1)

    return prediction1


def preprocessDataAndPredict_TSV(Genderin, Agein, Weightin, Heightin, Tempin, RHin, Vin, TMRTin, Areain, Seasonsin):
    test_data2 = [[Genderin, Agein, Weightin, Heightin, Tempin, RHin, Vin, TMRTin, Areain, Seasonsin]]


    test_data2 = np.array(test_data2)
    test_data2 = pd.DataFrame(test_data2)
    print(test_data2)
    #scaling data
    scaler = StandardScaler()
    test_data_scaled2 = scaler.fit_transform(test_data2)

    #predict
    prediction2 = tsvmodel.predict(test_data_scaled2)

    return prediction2

#for prediction in all_predictions:
#    print(prediction)


@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    return render_template('webapp2.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save('file')
        return render_template(".html", name='upload completed')

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