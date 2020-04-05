import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

import pandas as pd
import numpy as np
import scipy.stats as stats 
import matplotlib.pyplot as plt
import sklearn
from sklearn.ensemble import RandomForestRegressor 
from sklearn.model_selection import GridSearchCV,train_test_split 
from sklearn.metrics import mean_absolute_error


app = Flask(__name__)
data=pd.read_csv("Admission_Predict.csv");
admissions = data.drop('Serial No.',axis = 1)
x = admissions.drop('Chance_of_Admit',axis = 1)
y = admissions['Chance_of_Admit']
X_train,X_val,y_train,y_val = train_test_split(x,y,test_size = .30,random_state = 123)
model = RandomForestRegressor()
model.fit(X_train,y_train)
print('Mean absolute error for RF model: %0.4f' %mean_absolute_error(y_val,model.predict(X_val)))
new_ip = [[307,109,3,4,3,8,1]]
print(model.predict(new_ip))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]

    gre_score = request.form['gre_score']
    toefl_score = request.form['toefl_score']
    university_rating = request.form['university_rating']
    sop = request.form['sop']
    lor = request.form['lor']
    cgpa = request.form['cgpa']
    research = request.form['research']
        
    final_features = [[gre_score,toefl_score,university_rating,sop,lor,cgpa,research]]
    prediction = model.predict(final_features)
    print(final_features)


    return render_template('index.html', prediction_text='Chance of Admit is {}%'.format(prediction[0]*100))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
