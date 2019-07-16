import requests
import time
from requests.auth import HTTPBasicAuth
import random
h = {}
url = "https://192.168.1.20/api/v1/exec/disco"
login = "https://192.168.1.20/api/v1/login"

session = requests.Session()
session.trust_env = False
token = None
cookies = None
headers = {"Accept": "application/json"}
response = session.post(login, auth=HTTPBasicAuth('admin', 'admin'), headers=headers, verify=False)
print( login, response )
if response.status_code == 200:
    token_dic = response.json()
    cookies = response.cookies
    if token_dic != {}:
        token = token_dic.get('token')

h['Authorization'] = token
try:
    while(True):
        time.sleep(0.1)
        h["x-value"] = str( random.random() * 100)

        response = session.get(url, headers=h, auth=HTTPBasicAuth('admin', 'admin'), verify=False, cookies=cookies)
        # If the HTTP GET request can be served
        print(response.status_code)
        if response.status_code != 200:
            break
except:
    h["x-value"] = "0"
    session.get(url, headers=h, auth=HTTPBasicAuth('admin', 'admin'), verify=False, cookies=cookies)
