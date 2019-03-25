import json
import requests
import pprint

endpoint = "https://todo.ly/api/projects.json"
header = {
    "Content-Type": "application/json",
    "Authorization": "Basic Y2xhdWRpYS52aWxsYXJyb2VsQGZ1bmRhY2lvbi1qYWxhLm9yZzpGZWJyZXJvIQ=="

}
body = {"Content": "ClaudiaProject"}
res = requests.post(url=endpoint, data=json.dumps(body), headers=header)
print ("Create project status code: %s" % res.status_code)
print("Response")
pprint.pprint(res.json())

# PARA BUSCAR EL id
project_id = res_json ["Id"]
print ("Project ID %s" %project_id)

# hACER UN ASSERT
assert "Testing Create Project2" == res_json ["Content"], "Failed"
print ("FINISH")