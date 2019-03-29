import unittest

from automation.project import Project

id_1 = 0
id_2 = 0


class TestProject(unittest.TestCase):

    def tearDown(self):
        print "tearDown"
        if (id_1 > 0):
            Project.delete(id_1)
        if (id_2 > 0):
            Project.delete(id_2)

    def test_create_project(self):
        name = "new Project"
        response = Project.create(name)
        id_1 = self.get_id(response)
        self.assertEqual(response["status_code"], 200)
        self.assertEqual(name, self.get_name(response))

    def test_find_all(self):
        response1 = Project.create("test 1")
        response2 = Project.create("test 2")
        response = Project.readAll()
        self.assertTrue(response["status_code"] == 200)
        self.assertNotEqual(response["data"], None)
        self.assertNotEqual(response["data"], "")
        self.assertNotEqual(response["data"], {})
        self.assertTrue(len(response["data"]) > 1)
        self.loadIds(response1, response2)

    def test_find_project(self):
        response1 = Project.create("new Project to find")
        id_1 = self.get_id(response1)
        response2 = Project.read(id_1)
        self.assertTrue(response2["status_code"] == 200)
        self.assertTrue(id_1 == self.get_id(response2))

    def test_update_project_name(self):
        response1 = Project.create("new Project to find")
        id_1 = self.get_id(response1)
        response2 = Project.update(id_1, "Different name")
        self.assertTrue(response2["status_code"] == 200)
        self.assertTrue("Different name", self.get_name(response2))

    def test_delete(self):
        project_id = self.get_id(Project.create("test to delete"))
        response_delete = Project.delete(project_id)
        response_get = Project.read(project_id)
        self.assertTrue(response_delete["status_code"] == 200)
        self.assertTrue(response_get["status_code"] == 200)
        self.assertEqual(response_get["data"], "")

    def loadIds(self, response1, response2):
        id_1 = self.get_id(response1)
        id_2 = self.get_id(response2)

    def get_id(self, response):
        return response["data"]["Id"]

    def get_name(self, response):
        return response["data"]["Content"]
