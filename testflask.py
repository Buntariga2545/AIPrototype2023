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

with open(f'../AIPrototype2023/model/model.pkl', 'rb') as f:
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
    if request.method == "GET":
        return render_template("webapp.html")
    
    elif request.method == "POST":
        #get form data
        Gender = request.form.get('gender')
        Age = request.form.get('age')
        Weight = request.form.get('weight')
        Height = request.form.get('height')
        BMI = request.form.get('bmi')
        Temp= request.form.get('temp')
        RH = request.form.get('rh')
        V = request.form.get('v')
        TMRT = request.form.get('tmrt')
        Area = request.form.get('area')
        print(Gender,file=sys.stdout)
        print(Age,file=sys.stdout)
        print(Weight,file=sys.stdout)
        print(Height,file=sys.stdout)
        print(BMI,file=sys.stdout)
        print(Temp,file=sys.stdout)
        print(RH,file=sys.stdout)
        print(V,file=sys.stdout)
        print(TMRT,file=sys.stdout)
        print(Area,file=sys.stdout)

   
        try:
            prediction = preprocessDataAndPredict(Gender, Age, Weight, Height, BMI, Temp, RH, V, TMRT, Area)
            # Pass prediction to template
            return render_template('webapp2.html', prediction=prediction)


        except ValueError:
            return "Please Enter valid values"


#       print('เจอละ(POST)', file=sys.stdout)
#       Agein = request.form.get('ticketNum')
#       weightin = request.form.get('ticketNum')
#       print(Agein, file=sys.stdout)
#       print(weightin, file=sys.stdout)
#       return render_template("webapp.html", Age=Agein)

def preprocessDataAndPredict(Gender, Age, Weight, Height, BMI, Temp, RH, V, MRT, Area):
    #put all inputs in array
    test_data = pd.read_csv('data TSV.csv')
    print(test_data)

    #open file
    file = open("model.pkl","rb")

    #load trained model
    trained_model = joblib.load(file)

    #predict
    prediction = trained_model.predict(test_data)
    return prediction
    

#    result = model.predict([[gender, age, weight, height, bmi, temp,rh,v,tmrt,area]])[0]
#    return render_template('webapp2.html') #,gender=gender, age=age, weight=weight, heigh


@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == "POST":
        Genderin = request.form['Gender']
        Agein = request.form['Age']
        weightin = request.form['Weight']
        heightin = request.form['Height']
        BMIin = request.form['BMI']
        Tempin = request.form['Temp']
        RHin = request.form['RH']
        Vin = request.form['V']
        TMRTin = request.form['TMRT']
        areain = request.form['area']

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
    
#        return render_template("webapp2.html", prediction=predictions)


#        try:
#            prediction = preprocessDataAndPredict(Age, Weight, Height, BMI, Temp, RH, V, MRT)
            # Pass prediction to template
#            return render_template('webapp2.html', prediction=prediction)
#        except ValueError:
#            return "Please Enter valid values"
 #   else:
        # Handle GET request
 #       return render_template('webapp2.html')

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