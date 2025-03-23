endpoint = 'http://6fe1d2f6-b11c-40a9-8a40-b043185f0482.eastus2.azurecontainer.io/score'  # Replace with your endpoint
key = 'injhva76MYg2Sfec50eTjoqVoME4tEEi'  # Replace with your key

import json
import urllib.request

data = {
    "Inputs": {
        "WebServiceInput0":
            [
                {
                    'PatientID': 1882185,
                    'Pregnancies': 9,
                    'PlasmaGlucose': 104,
                    'DiastolicBloodPressure': 51,
                    'TricepsThickness': 7,
                    'SerumInsulin': 24,
                    'BMI': 27.36983156,
                    'DiabetesPedigree': 1.3504720469999998,
                    'Age': 43,
                },
            ],
    },
    "GlobalParameters": {
    }
}

body = str.encode(json.dumps(data))
body = b''
headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + key)}

req = urllib.request.Request(endpoint, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    json_result = json.loads(result)
    output = json_result["Results"]["WebServiceOutput0"][0]
    print('Patient: {}\nPrediction: {}\nProbability: {:.2f}'.format(output["PatientID"],
                                                                    output["DiabetesPrediction"],
                                                                    output["Probability"]))
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers to help debug 
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
