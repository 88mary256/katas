import json
import requests
import pprint

host = "https://todo.ly/api/"

def create(name):
    endpoint = host + "projects.json"
    header = {"Authorization": "Basic Z2F0aXRhMDEwMS5teG1AZ21haWwuY29tOjEyMzQ1Njc4",
              "Content-Type": "application/json"}
    # name = "My 2nd project"
    body = {"Content": name}
    print "Creating project with name " + name
    response = requests.post(url=endpoint, data=json.dumps(body), headers=header)
    response_json = response.json()
    print("Create Project status code: %s" % response.status_code)
    pprint.pprint(response.json())

    assert response.status_code == 200, "Failed"
    assert name == response_json["Content"], "Failed"
    return response_json["Id"]

def readAll():
    endpoint = host + "projects.json"
    header = {"Authorization": "Basic Z2F0aXRhMDEwMS5teG1AZ21haWwuY29tOjEyMzQ1Njc4"}
    print "reading all projects"
    response = requests.get(url=endpoint, headers=header)
    response_json = response.json()
    pprint.pprint(response.json())
    assert response.status_code == 200, "Failed"
    return response_json

#https://todo.ly/api/projects/[id].format
def read(id):
    endpoint = host + "projects/"+str(id)+".json"
    header = {"Authorization": "Basic Z2F0aXRhMDEwMS5teG1AZ21haWwuY29tOjEyMzQ1Njc4"}
    print "read a project with id: " + str(id)
    response = requests.get(url=endpoint, headers=header)
    response_json = response.json()
    pprint.pprint(response.json())
    assert response.status_code == 200, "Failed"
    assert int(id) == int(response_json["Id"]), "Failed"
    return response_json


def update(id, name):
    endpoint = host + "projects/"+str(id)+".json"
    header = {"Authorization": "Basic Z2F0aXRhMDEwMS5teG1AZ21haWwuY29tOjEyMzQ1Njc4",
              "Content-Type": "application/json"}
    body = {"Content": name}
    response = requests.put(url=endpoint, data=json.dumps(body), headers=header)
    response_json = response.json()
    pprint.pprint(response.json())
    assert response.status_code == 200, "Failed"
    assert int(id) == int(response_json["Id"]), "Failed"
    assert name == response_json["Content"], "Failed"
    return response_json


def delete(id):
    endpoint = host + "projects/"+str(id)+".json"
    header = {"Authorization": "Basic Z2F0aXRhMDEwMS5teG1AZ21haWwuY29tOjEyMzQ1Njc4"}
    response = requests.delete(url=endpoint, headers=header)
    response_json = response.json()
    pprint.pprint(response.json())
    assert response.status_code == 200, "Failed"
    assert int(id) == int(response_json["Id"]), "Failed"
    response_get = requests.get(url=endpoint, headers=header)
    print response_get.content
    #pprint.pprint(response_get.json())
    assert response_get.status_code == 200, "Failed"
    assert response_get.content == "", "Failed"


def main():
    id = create("New project")
    readAll()
    read(id)
    update(id,"a different project name")
    delete(id)
    print "finish project CRUD"


main()
