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


app = Flask(__name__)

#with open(f'../AIPrototype2023/model/model.pkl', 'rb') as f:
#    model = load(f)
with open(f'../AIPrototype2023/model/model_tsv.pk', 'rb') as f:
    model_tsv = load(f)
with open(f'../AIPrototype2023/model/tamodel.pk', 'rb') as f:
    model_ta = load(f)

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
    
#        Gender = request.form.get('gender')
#        Area = request.form.get('area')
#        print(Gender,file=sys.stdout)
#        print(Area,file=sys.stdout)
    
    elif request.method == "POST":
        Genderin = request.form.get('Gender')
        print('Gender = ', Genderin, file=sys.stdout)
        Agein = request.form.get('Age')
        print('Age = ', Agein, file=sys.stdout)      
        Weightin = request.form.get('Weight') 
        print('Weight = ', Weightin, file=sys.stdout)
        Heightin = request.form.get('Height')
        print('Height = ', Heightin, file=sys.stdout)
        BMIin = request.form.get('BMI')
        print('BMI = ', BMIin, file=sys.stdout)
        Tempin = request.form.get('Temp')
        print('Temp = ', Tempin, file=sys.stdout)
        RHin = request.form.get('RH')
        print('RH = ', RHin, file=sys.stdout)
        Vin = request.form.get('V')
        print('V = ', Vin, file=sys.stdout)
        TMRTin = request.form.get('TMRT')
        print('TMRT = ', TMRTin, file=sys.stdout)
        Areain = request.form.get('Area')
        print('Area = ', Areain, file=sys.stdout)
        Seasonsin = request.form.get('Seasons')
        print('Seasons = ', Seasonsin, file=sys.stdout)


        try:
            prediction_ta = preprocessDataAndPredict(Genderin, Agein, Weightin, Heightin, BMIin, Tempin, RHin, Vin, TMRTin, Areain, Seasonsin)
            prediction_tsv = preprocessDataAndPredict(Genderin, Agein, Weightin, Heightin, BMIin, Tempin, RHin, Vin, TMRTin, Areain, Seasonsin)
            # Pass predictions to template
            return render_template('webapp2.html', prediction_ta=prediction_ta, prediction_tsv=prediction_tsv)
        except ValueError:
            return "Please Enter valid values"


def preprocessDataAndPredict(Genderin, Agein, Weightin, Heightin, BMIin, Tempin, RHin, Vin, TMRTin, Areain, Seasonsin):
    #put all inputs in array
#   test_data = pd.read_csv('data TSV.csv')
    test_data1 = [[Genderin, Agein, Weightin, Heightin, BMIin, Tempin, RHin, Vin, TMRTin, Areain, Seasonsin]]
    print(test_data1)

    test_data1 = np.array(test_data1)
    test_data1 = pd.DataFrame(test_data1)
    print(test_data1)

    #open file
#    file = open("model.pkl","rb")

    #load trained model
#    trained_model = joblib.load(file)

    #predict
    prediction_ta = model_ta.predict(test_data1)
    return prediction_ta


def preprocessDataAndPredict(Genderin, Agein, Weightin, Heightin, BMIin, Tempin, RHin, Vin, TMRTin, Areain, Seasonsin):
    #put all inputs in array
#   test_data = pd.read_csv('data TSV.csv')
    test_data2 = [[Genderin, Agein, Weightin, Heightin, BMIin, Tempin, RHin, Vin, TMRTin, Areain, Seasonsin]]
    print(test_data2)

    test_data2 = np.array(test_data2)
    test_data2 = pd.DataFrame(test_data2)
    print(test_data2)

    #open file
#    file = open("model.pkl","rb")

    #load trained model
#    trained_model = joblib.load(file)

    #predict
    prediction_tsv = model_tsv.predict(test_data2)
    return prediction_tsv

#    prediction = model_ta.predict(test_data)
#    prediction = model_tsv.predict(test_data)
#    return prediction
    

#    result = model.predict([[gender, age, weight, height, bmi, temp,rh,v,tmrt,area]])[0]
#    return render_template('webapp2.html') #,gender=gender, age=age, weight=weight, heigh


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