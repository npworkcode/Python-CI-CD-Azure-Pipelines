from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging
import sys

import pandas as pd
from sklearn.externals import joblib

from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

logging.basicConfig(filename='applog.txt', filemode='a')
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

def scale(payload):
    """Scales Payload"""

    LOG.info('Scaling Payload: %s payload')
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    LOG.info('Scaled Adhoc Predict: %s scaled_adhoc_predict')
    return scaled_adhoc_predict

@app.route("/")
def home():
    html = "<h3>Sklearn Prediction Home</h3>"
    LOG.info('HTML home result: %s', html.format(format))
    return html.format(format)

# TO DO:  Log out the prediction value
@app.route("/predict", methods=['POST'])
def predict(): # pragma: no cover
    """Performs an sklearn prediction

    input looks like:
            {
    "CHAS":{
      "0":0
    },
    "RM":{
      "0":6.575
    },
    "TAX":{
      "0":296.0
    },
    "PTRATIO":{
       "0":15.3
    },
    "B":{
       "0":396.9
    },
    "LSTAT":{
       "0":4.98
    }

    result looks like:
    { "prediction": [ 20.35373177134412 ] }

   

    """

    try:
        with open("boston_housing_prediction.joblib",'rb') as f:
            clf = joblib.load(f)
    except UnicodeDecodeError:
        return "Cannot decode Unicode file"
    except ValueError as inst:
        print(type(inst))
        print(inst.args)
        print(inst)
        return("Value error occurred")
    except IOError:
        return "Cannot open data file"
    except RuntimeError:
        print ("Unexpected error:", sys.exc_info()[0])
        return "Unexpected Error"
    else:
        json_payload = request.json
        LOG.info("JSON payload: %s json_payload")
        inference_payload = pd.DataFrame(json_payload)
        LOG.info("inference payload DataFrame: %s inference_payload")
        scaled_payload = scale(inference_payload)
        prediction = list(clf.predict(scaled_payload))
        return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
