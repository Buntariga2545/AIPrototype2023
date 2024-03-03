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

with open(f'model/model.pk', 'rb') as f:
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
    if request.method == "POST":
       print('Results', file=sys.stdout)

       Genderin = request.form.get('Gender')
       print('Gender = ', Genderin, file=sys.stdout)
       Agein = request.form.get('Age')
       print('Age = ', Agein, file=sys.stdout)      
       weightin = request.form.get('Weight') 
       print('Weight = ', weightin, file=sys.stdout)
       heightin = request.form.get('Height')
       print('Height = ', heightin, file=sys.stdout)
       BMIin = request.form.get('BMI')
       print('BMI = ', BMIin, file=sys.stdout)
       Tempin = request.form.get('Temp')
       print('Temp = ', Tempin, file=sys.stdout)
       RHin = request.form.get('%RH')
       print('%RH = ', RHin, file=sys.stdout)
       Vin = request.form.get('V')
       print('V = ', Vin, file=sys.stdout)
       MRTin = request.form.get('MRT')
       print('MRT = ', MRTin, file=sys.stdout)
       arein = request.form.get('are')
       print('are = ', arein, file=sys.stdout)

       return render_template("webapp.html", data = [Genderin, Agein, weightin, heightin, BMIin, Tempin, RHin, Vin, MRTin, arein])

    elif request.method == "GET":
       print('Results', file=sys.stdout)
       Agein = request.form.get('Age')
       print('Age = ', Agein, file=sys.stdout)   
       weightin = request.form.get('Weight')
       print('Weight = ', weightin, file=sys.stdout)
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


@app.route('/predict/', methods = ['GET', 'POST'])
def predict():
    if request.method == "POST":
        # Get form data
        Age = request.form.get('Age')
        Weight = request.form.get('Weight')
        Height = request.form.get('Height')
        BMI = request.form.get('BMI')
        Temp = request.form.get('Temp')
        RH = request.form.get('%RH')
        V = request.form.get('V')
        MRT = request.form.get('MRT')

        test_data = pd.DataFrame([[Age, Weight, Height, BMI, Temp, RH, V, MRT]],
                                    columns=['Age', 'Weight', 'Height', 'BMI', 
                                         'Temp', 'RH', 'V', 'MRT'],
                                    dtype='float',
                                    index=['input'])
        
        prediction = model.predict(test_data)[0]
        print(prediction)

        return render_template('webapp2.html', original_input={'Age': Age, 'Weight': Weight, 'Height': Height, 'BMI': BMI, 
                                'Temp': Temp, '%RH': RH, 'V': V, 'MRT': MRT},
                                result=prediction)
    
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
    test_data = np.array([[Age, Weight, Height, BMI, Temp, RH, V, MRT]])
    
    # Open file
    file = open("model.pk","rb")
    # Load trained model
    trained_model = joblib.load(file)
    # Predict
    prediction = trained_model.predict(test_data)
    
    return prediction
    
#def preprocessDataAndPredict(Age, Weight, Height, BMI, Temp, RH, V, MRT):
    #put all inputs in array
    test_data = pd.read_csv('test_data.csv')
    print(test_data)
    #open file
    file = open("model.pk","rb")
    #load trained model
    trained_model = joblib.load(file)
    #predict
    prediction = trained_model.predict(test_data)
    return render_template('webapp2.html', prediction = prediction)


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