import json
import requests
# local url
url = "http://127.0.0.1:5000"

# sample data

data = {
    'Pclass':3,
    'Age': 2,
    'SibSp':1,
    'Fare':50
}

data = json.dumps(data)
print("Sending request!")
send_request = requests.post(url, data)
print(send_request.__dir__)

try:
    print(send_request.json())
except:
    print("wrong reply!")