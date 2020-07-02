import requests

# islanding
islanding = requests.get(
    'https://my-json-server.typicode.com/iti/mockcontroller/islanding').json()
print(islanding)

# system_status
systemStatus = requests.get(
    'https://my-json-server.typicode.com/iti/mockcontroller/system_status').json()
print(systemStatus)

# meters
meters = requests.get(
    'https://my-json-server.typicode.com/iti/mockcontroller/meters').json()
print(meters)

# alerts
alerts = requests.get(
    'https://my-json-server.typicode.com/iti/mockcontroller/alerts').json()
print(alerts)

# controller
controller = requests.get(
    'https://my-json-server.typicode.com/iti/mockcontroller/controller').json()
print(controller)
