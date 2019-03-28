import json
import pprint
import requests

#http://todo.ly/apiwiki/?projects/todo-ly-rest-api-method-put-projectsid

endpoint = "https://todo.ly/api/projects/"
ID="3782757"
header = {"Content-Type": "application/json",
          "Authorization": "Basic cnJjaC5jcjhAZ21haWwuY29tOmM2NDI0NzgyUg=="}
newbody = {"Content": "Testing MODIFY huachimingo"}

res = requests.post(url=endpoint+ID+".json", data=json.dumps(newbody), headers=header)

print("Modify Project status code: %s" % res.status_code)
print("Response")
res_json = res.json()
pprint.pprint(res_json)

project_id = res_json["Id"]
print ("project id %s " % project_id)
