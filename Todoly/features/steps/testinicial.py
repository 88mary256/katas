from behave import *
import json
import pprint
import requests
#from Todoly.src.projectServices.ApiTestingPOST import Create


@given("I made connection")
def step_impl(context):
    print(u'STEP: Given I made connection')


@when("I create project with data {item}")
def step_create(context, item ):

    #Create.create_todolyproject(item)
    def create_todolyProject(projectName):
        endpoint = "https://todo.ly/api/projects.json"
        header = {"Content-Type": "application/json",
                  "Authorization": "Basic cnJjaC5jcjhAZ21haWwuY29tOmM2NDI0NzgyUg=="}
        body = {"Content": projectName}

        res = requests.post(url=endpoint, data=json.dumps(body), headers=header)

        print("Create Project status code: %s" % res.status_code)
        print("Response:")
        res_json = res.json()
        pprint.pprint(res_json)

        project_id = res_json["Id"]
        print ("project id %s " % project_id)

    create_todolyProject(item)


    print("STEP: When I create project with data: {}".format(item))



@then("The create project status is 204")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: Then The create project status is 204')


@step('Project Name is "Project 1"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: And Project Name is "Project 1"')

