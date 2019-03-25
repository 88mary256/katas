# pip install <python package install>
# pip install request
# package install>
# C:\Python27\Scripts ese path se anade a las variables de entorno

import json
import pprint
import requests

endpoint = "https://todo.ly/api/projects.json"
header = {"Content-Type": "application/json",
          "Authorization": "Basic cnJjaC5jcjhAZ21haWwuY29tOmM2NDI0NzgyUg=="}
body = {"Content": "Testing Create Project LUNES"}

res = requests.post(url=endpoint, data=json.dumps(body), headers=header)

print("Create Project status code: %s" % res.status_code)
print("Response")
res_json = res.json()
pprint.pprint(res_json)

project_id = res_json["Id"]
print ("project id %s " % project_id)
assert "Testing Create Project 2" == res_json["Content"], "Failed"
