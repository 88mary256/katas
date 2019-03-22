# katas

# pip install <python package name>
# pip install requests
# C:\Python27\Scripts
import json
import pprint

import requests

endpoind = "https://todo.ly/api/projects.json"
header = {
    "Content-Type": "application/json",
    "Authorization": "Basic cGVwaXRvMUBtYWlsaW5hdG9yLmNvbTpQQHNzdzByZA=="
}

body = {"Content": "Testing Create Project 1"}

res = requests.post(url=endpoind, data=json.dumps(body), headers=header)

print("Create Project status code: %s" % res.status_code)
print("Response")
pprint.pprint(res.json())
