import unittest

from examen.py.register_students import *
from examen.py.student import Student


class TestRegisterStudents(unittest.TestCase):
    def setUp(self):
        register_subject(Subject(1, "art"))
        register_subject(Subject(2, "language"))

    def test_register_subject_with_object(self):
        before = len(get_subjects())
        subject = Subject(3, "math")
        register_subject(subject)
        after = len(get_subjects())
        self.assertTrue(before < after)
        self.assertTrue(subject.id in get_subjects())

    def test_register_subject_with_parametters(self):
        before = len(get_subjects())
        id = 4
        register_subject_with_data(id, "gym")
        after = len(get_subjects())
        self.assertTrue(before < after)
        self.assertTrue(id in get_subjects())

    def test_register(self):
        before_subject1 = len(get_students_in_subject(1))
        before_subject2 = len(get_students_in_subject(2))
        register_student_in_subject(1, Student(2006314, "marines"))
        register_student_in_subject(2, Student(2004314, "maya"))
        register_student_in_subject(1, Student(2006304, "claudia"))
        register_student_in_subject(1, Student(2006326, "carlos"))
        after_subject1 = len(get_students_in_subject(1))
        after_subject2 = len(get_students_in_subject(2))
        self.assertTrue(before_subject1 < after_subject1)
        self.assertTrue(before_subject2 < after_subject2)
