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
'''<Response [200]>
{u'Children': [],
 u'Collapsed': False,
 u'Content': u'My 2nd project',
 u'Deleted': False,
 u'Icon': 0,
 u'Id': 3782188,
 u'IsOwnProject': True,
 u'IsProjectShared': False,
 u'IsShareApproved': False,
 u'ItemOrder': 13,
 u'ItemType': 2,
 u'ItemsCount': 0,
 u'LastSyncedDateTime': u'/Date(1553288790082)/',
 u'LastUpdatedDate': u'/Date(1553288790083)/',
 u'ParentId': None,
 u'ProjectShareOwnerEmail': None,
 u'ProjectShareOwnerName': None,
 u'SyncClientCreationId': None}
3782188
'''

'''
tarea crear read update delete

hacer 1 proyecto con su subproyecto y una tarea en el subprojecto
Page Object Model: representacion abstracta de la pagina web application
Json schema validator
Gherkin: para representar un escenario del BDT,es ele lenguaje que cucumber entiende
Behave tool nos permite correr nuestros escenarios

Pivotaltracker.com 
research cerking keywords
leer hasta la diapositiva 20

top gerkin
steps python
pages services python
helpers setup python
'''