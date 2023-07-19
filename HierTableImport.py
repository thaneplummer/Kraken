#Need to install requests package for python
#easy_install requests
import requests
import json

#Classes
class ReqOb:
    def __init__(self, user, pwd, headers) -> None:
        self.user = user
        self.pwd = pwd
        self.headers = headers
        
    def get(self, url):
        response = requests.get(url, auth=(self.user, self.pwd), headers=self.headers)
        if response.status_code != 200: 
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        return response
    
    def post(self, url, payload):
        response = requests.post(url, auth=(self.user, self.pwd), headers=self.headers, payload=payload)

# Set the request parameters
qTable = 'x_380321_cmdpost_element'
parameters = {'sysparm_exclude_reference_link':'True', 'sysparm_limit':'1', 'hierarchy': '7ff1acc847d91110d396c789826d433c', 'u_level': 3}
paramLink = '&'.join('%s=%s' %(k,v) for k,v in parameters.items())
url = 'https://dev57368.service-now.com/api/now/table/%s?%s' %(qTable, paramLink)

# Eg. User name="admin", Password="admin" for this code sample.
user = 'arendil.plummer'
pwd = 'Only4ankp!'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
json.dump(data, r'stat.json')