import json
import requests
import pprint

endpoint = "https://todo.ly/api/projects/3782161.json"
header = {
    "Content-Type": "application/json",
    "Authorization": "Basic Y2xhdWRpYS52aWxsYXJyb2VsQGZ1bmRhY2lvbi1qYWxhLm9yZzpGZWJyZXJvIQ=="

}
body = {"Content": "claudia"}
res = requests.get(url=endpoint, data=json.dumps(body), headers=header)
print ("Get ID project status code: %s" % res.status_code)
print("Response")
pprint.pprint(res.json())

