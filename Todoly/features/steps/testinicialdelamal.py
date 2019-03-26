from behave import *




@given("I made connection")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: Given I made connection')


@when("I create project with data")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: When I create project with data')


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

@when(u'I create project with data "Project1"')
def step_impl(context):
    print(u'STEP: When I create project with data "Project1"')



