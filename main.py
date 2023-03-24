from flask import Flask, jsonify, request
import joblib  
import pandas as pd
import numpy as np
app = Flask(__name__)
@app.route('/crop', methods=['POST'])
def predict():
     req_data = request.json
     n = req_data["N"]
     p = req_data["P"]
     k = req_data["K"]
     temp = req_data["temp"]
     humidity = req_data["humidity"]
     ph = req_data["ph"]
     rain = req_data["rain"]
     data = np.array([[n,p, k, temp, humidity, ph, rain]])
     prediction = clf.predict(data)
     return jsonify({'prediction': prediction[0]})

@app.route('/fertilizer',methods=['POST'])
def fertilizer():
     req_data = request.json

     n = req_data["N"]
     p = req_data["P"]
     k = req_data["K"]
     temp = req_data["temp"]
     humidity = req_data["humidity"]
     moisture = req_data["moisture"]
     soil = req_data["soil"]
     crop = req_data["crop"]

     data_to_pred = np.array([[temp,humidity,moisture,soil,crop,n,k,p]])
     df = pd.DataFrame(data_to_pred, columns = ['Temparature','Humidity','Moisture','Soil Type','Crop Type','Nitrogen','Potassium','Phosphorous'])
     res = fertilizerModel.predict(df)

     return jsonify({'prediction': res[0]})
     


@app.route('/test')
def test():
    return jsonify({'prediction': 'pass'})
if __name__ == '__main__':
     clf = joblib.load('RandomForest.pkl')
     fertilizerModel = joblib.load('fertilizer.pkl')
     app.run(port=8080)