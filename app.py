import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)

## Load model from pickled file
with open('regmodel.pkl', 'rb') as f:
    reg_model=pickle.load(f)

with open('scaling.pkl', 'rb') as f:
    scaler=pickle.load(f)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict_api',methods=['POST']) # POST not allow direct calling from browser
def predict_api():
    data=request.json["data"] ## input in json format in data key
    #print(data)
    print(list(data.values()))
    print(np.array(list(data.values())))
    #print(np.array(list(data.values())).reshape(1,-1))
    new_data=scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output=reg_model.predict(new_data)
    print(output[0])
    return jsonify(output[0])

if __name__=="__main__":
    app.run(debug=True)


