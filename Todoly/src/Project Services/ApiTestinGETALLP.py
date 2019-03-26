import json
import pprint
import requests

#http://todo.ly/apiwiki/?projects/todo-ly-rest-api-method-get-projects

endpoint = "https://todo.ly/api/projects.json"
#ID="3782757"
user="rrch.cr8@gmail.com"
password="c6424782R"

r=requests.get(url=endpoint,auth=(user, password))


print("Get Project status code: %s" % r.status_code)
print("Response hacia mi:")
res_json = r.json()
pprint.pprint(res_json)

