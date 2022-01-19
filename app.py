from flask import Flask, render_template, request
import requests
import pickle
import os
import pandas as pd
import numpy as np
import sklearn


app = Flask(__name__)
model = pickle.load(open('/Users/karunakar/Documents/Data Science/VK/SPYDER/rent.pkl','rb'))
@app.route('/',methods=['GET'])
def Home(): 
    return render_template('rent.html')

@app.route("/predict", methods=['POST'])
def predict():
    print('no')
        
    if request.method == 'POST':

        Type_ = str(request.form['type'])
        print("t")
        Bedrooms = str(request.form['bedrooms'])
        print("be")
        Bathrooms = str(request.form['bathrooms'])
        print("ba")
        Furnishing = str(request.form['furnishing'])
        print("f")
        ListedBy = str(request.form['listed by'])
        print("l")
        SuperBuiltupArea = str(request.form['super builtup area (ft²)'])
        print("sba")
        CarpetArea = str(request.form['carpet area (ft²)'])
        print("ca")
        BachelorsAllowed = str(request.form['bachelors allowed'])
        print("ba")
        Maintenance = str(request.form['maintenamaintenance (monthly)'])
        print("mm")
        TotalFloors = str(request.form['total floors'])
        print("tf")
        Carparking = str(request.form['car parking'])
        print("cp")
        Floorno= str(request.form['floor no'])
        print("fn")
        Facing= str(request.form['facing'])
        print("face")
        City= str(request.form['city'])
        print("c")
        State= str(request.form['state'])
        print("s")
       
      
       
        prediction=model.predict(np.array([[Type_, Bedrooms, Bathrooms, Furnishing, ListedBy, SuperBuiltupArea,CarpetArea,
        BachelorsAllowed,Maintenance,TotalFloors,Carparking, Floorno, Facing, State, City]]))
        output=round(prediction[0],2)
        if output<0:
            return render_template('rent.html',prediction="Sorry no house for rent")
        else:
            return render_template('rent.html',prediction="price of the house ₹ {} ".format(output))
    else:
        return render_template('rent.html')

if __name__ == "__main__":
   port = int(os.environ.get('PORT' ,9000))
   app.run(host='0.0.0.0', port=port)
