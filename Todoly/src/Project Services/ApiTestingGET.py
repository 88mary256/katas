import json
import pprint
import requests

#http://todo.ly/apiwiki/?projects/todo-ly-rest-api-method-get-projectsid

endpoint = "https://todo.ly/api/projects/"
ID="3782757"
user="rrch.cr8@gmail.com"
password="c6424782R"

r=requests.get(url=endpoint+ID+".json",auth=(user, password))


print("Get Project status code: %s" % r.status_code)
print("Response hacia mi:")
res_json = r.json()
pprint.pprint(res_json)

project_date = res_json["LastSyncedDateTime"]
print ("project date is: %s " % project_date)

project_name = res_json["Content"]
print ("project content is: %s " % project_name)
