import json
import requests


def make_request(model, data):
    input_data_json = json.dumps({
        "signature_name": "serving_default",
        "inputs": data
    })

    url = 'http://translation-model.herokuapp.com/v1/models/' + model + ':predict'
    response = requests.post(url, data=input_data_json)
    response.raise_for_status()
    response = response.json()
    prediction = response["outputs"]

    return prediction