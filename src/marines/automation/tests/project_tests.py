import unittest

from automation.project import Project


class TestProject(unittest.TestCase):
    id = 0
    def tearDown(self):
        if (id>0):
            Project.delete(id)


    def test_find_user_id(self):
        name = "new Project"
        print "Creating project with name " + name
        response = Project.create(name)
        id = response["id"]
        self.assertEqual(response["status_code"], 200)
        self.assertEqual(name, response["Content"])

