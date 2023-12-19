import json
import pickle

from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

app = Flask(__name__)

# Load the model
ridgemodel = pickle.load(open('ridgemodel.pkl', 'rb'))
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    new_data_json = request.json['data']
    data2 = new_data_json.get('data', {})
    df_new = pd.DataFrame([data2])
    print(df_new)
    
    # Use preprocessor
    new_data = preprocessor.transform(df_new)  # Use transform instead of fit_transform
    output = ridgemodel.predict(new_data)
    print(output[0])
    
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    
    # Use preprocessor instead of fitting it again
    final_input = preprocessor.transform(np.array([data]))
    print(final_input)
    
    output = ridgemodel.predict(final_input)[0]
    
    return render_template("home.html", prediction_text="The mark of math prediction is {}".format(output))

if __name__ == "__main__":
    app.run(debug=True)
