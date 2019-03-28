import json
import requests
import pprint

from automation.request_handler import RequestHandler

request_handler = RequestHandler(
    header={"Authorization": "Basic Z2F0aXRhMDEwMS5teG1AZ21haWwuY29tOjEyMzQ1Njc4", "Content-Type": "application/json"},
    base_url="https://todo.ly/api/")


class Project():

    @staticmethod
    def create(name):
        print "Creating project with name " + name
        response = request_handler.post_request("projects.json", {"Content": name})
        pprint.pprint(response.json())
        return {"status_code": response.status_code, "data": response.json()}

    @staticmethod
    def readAll():
        print "reading all projects"
        response = request_handler.get_request("projects.json")
        pprint.pprint(response.json())
        return {"status_code": response.status_code, "data": response.json()}

    @staticmethod
    def read(id):
        # https://todo.ly/api/projects/[id].format
        print "Read a project with id: " + str(id)
        response = request_handler.get_request("projects/" + str(id) + ".json")
        data = response.content
        print(response.content)
        if response.content != "":
            data = response.json()
            pprint.pprint(response.json())
        return {"status_code": response.status_code, "data": data}

    @staticmethod
    def update(id, name):
        print "Updating project with name " + name
        response = request_handler.put_request("projects/" + str(id) + ".json", {"Content": name})
        pprint.pprint(response.json())
        return {"status_code": response.status_code, "data": response.json()}

    @staticmethod
    def delete(id):
        print "Deleting project with id " + str(id)
        response = request_handler.delete_request("projects/" + str(id) + ".json")
        pprint.pprint(response.json())
        return {"status_code": response.status_code, "data": response.content}
