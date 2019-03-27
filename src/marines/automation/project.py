import json
import requests
import pprint



class Project():

    @staticmethod
    def create(name):
        print "Creating project with name " + name
        endpoint = host + "projects.json"
        # name = "My 2nd project"
        body = {"Content": name}
        response = requests.post(url=endpoint, data=json.dumps(body), headers=header)
        response_json = response.json()
        pprint.pprint(response.json())
        return {"id": response_json["Id"], "status_code": response.status_code, "name": response_json["Content"]}

    @staticmethod
    def readAll():
        endpoint = host + "projects.json"
        print "reading all projects"
        response = requests.get(url=endpoint, headers=header)
        pprint.pprint(response.json())
        assert response.status_code == 200, "Failed"
        return response.json()

    # https://todo.ly/api/projects/[id].format
    @staticmethod
    def read(id):
        endpoint = host + "projects/" + str(id) + ".json"
        print "read a project with id: " + str(id)
        response = requests.get(url=endpoint, headers=header)
        response_json = response.json()
        pprint.pprint(response.json())
        assert response.status_code == 200, "Failed"
        assert int(id) == int(response_json["Id"]), "Failed"
        return response_json

    @staticmethod
    def update(id, name):
        endpoint = host + "projects/" + str(id) + ".json"
        body = {"Content": name}
        response = requests.put(url=endpoint, data=json.dumps(body), headers=header)
        response_json = response.json()
        pprint.pprint(response.json())
        assert response.status_code == 200, "Failed"
        assert int(id) == int(response_json["Id"]), "Failed"
        assert name == response_json["Content"], "Failed"
        return response_json

    @staticmethod
    def delete(id):
        endpoint = host + "projects/" + str(id) + ".json"
        response = requests.delete(url=endpoint, headers=header)
        response_json = response.json()
        pprint.pprint(response.json())
        assert response.status_code == 200, "Failed"
        assert int(id) == int(response_json["Id"]), "Failed"
        response_get = requests.get(url=endpoint, headers=header)
        print response_get.content
        # pprint.pprint(response_get.json())
        assert response_get.status_code == 200, "Failed"
        assert response_get.content == "", "Failed"
