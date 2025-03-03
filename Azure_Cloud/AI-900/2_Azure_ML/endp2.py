import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
x = [[1,1,2022,1,0,6,0,2,0.344167,0.363625,0.805833,0.160446],

     [2,1,2022,1,0,0,0,2,0.363478,0.353739,0.696087,0.248539],

     [3,1,2022,1,0,1,1,1,0.196364,0.189405,0.437273,0.248309],

     [4,1,2022,1,0,2,1,1,0.2,0.212122,0.590435,0.160296],

     [5,1,2022,1,0,3,1,1,0.226957,0.22927,0.436957,0.1869]]

body = json.dumps({"data": x})
body = b'{body}'
# body = str.encode(json.dumps(data))

url = 'http://0e79049f-e9d3-42e1-87f8-9c9f68049803.eastus2.azurecontainer.io/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'AJioqUQ53gFdrglEv5UHHffyOxFuA5rB'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
