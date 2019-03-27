import json
import requests
import pprint

#class AutomationForTodoLy():

host = "https://todo.ly/api/"
#def create_project():
endpoint = host + "projects.json"
header = {"Authorization": "Basic Z2F0aXRhMDEwMS5teG1AZ21haWwuY29tOjEyMzQ1Njc4",
          "Content-Type": "application/json"}
name = "My 2nd project"
body = {"Content": name}
response = requests.post(url=endpoint, data=json.dumps(body),headers=header)
response_json = response.json()
print("Create Project status code: %s" % response.status_code)
print response
pprint.pprint(response.json())
print response.json()["Id"]

assert name == response_json["Content"], "Failed"
