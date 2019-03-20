class Subject:
    '''   def __init__(self, id, name, students):
           self.id = id
           self.name = name
           self.students = students
   '''

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
