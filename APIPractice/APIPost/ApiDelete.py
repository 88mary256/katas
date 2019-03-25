import json
import requests
import pprint

endpoint = "https://todo.ly/api/projects/3782162.json"
header = {
    "Content-Type": "application/json",
    "Authorization": "Basic Y2xhdWRpYS52aWxsYXJyb2VsQGZ1bmRhY2lvbi1qYWxhLm9yZzpGZWJyZXJvIQ=="

}
body = { }
res = requests.delete(url=endpoint, data=json.dumps(body), headers=header)
print ("Create project status code: %s" % res.status_code)
print("Response")
pprint.pprint(res.json())


