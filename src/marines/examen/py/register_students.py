from examen.py.subject import Subject

subjects = {}


def register_student_in_subject(sub_id, student):
    if (sub_id in subjects):
        subjects[sub_id] = Subject(id, "new subject", [student])
    else:
        subject = subjects[sub_id]
        subject.students = student


def register_subject_with_data(id, name):
    subjects[id] = Subject(id, name)


def register_subject(subject):
    subjects[subject.id] = subject


def get_subjects():
    return subjects


def get_students_in_subject(id):
    if (id not in subjects):
        return 0
    subject = subjects[id]
    return len(subject.students)
