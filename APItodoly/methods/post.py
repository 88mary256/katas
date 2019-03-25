import requests
import json
import pprint


endpoint = "https://todo.ly/api/projects.json"
header = {"Content-Type": "application/json",
          "Authorization": "Basic cGVkcm9AbWFpbGluYXRvci5jb206dG9kb2x5",
          "cache-control": "no-cache"
          }

body = {"Content": "Testing methods project"}
res = requests.post(url=endpoint, data=json.dumps(body), headers=header)
print ("methods project status coode: %s" % res.status_code)
print ("Response")
res_json = res.json()
pprint.pprint(res.json())

project_id = res_json["Id"]
print ("project_id %s" % project_id)

assert "Testing methods project" == res_json["Content"], "Failed"

print "EOF"