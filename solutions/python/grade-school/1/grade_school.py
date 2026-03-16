class Student:
    def __init__(self, name: str, grade: int):
        self.name = name
        self.grade = grade

    def __str__(self):
        return self.name
    
    def __eq__(self, value):
        return isinstance(value, Student) and self.name == value.name  
      
    def __hash__(self):
        return hash(self.name)


class School:
    def __init__(self):
        self.students = set()
        self.students_added = list()

    def add_student(self, name: str, grade: int):
        student = Student(name, grade)
        length_before = len(self.students)
        self.students.update({student})
        length_after = len(self.students)

        if length_after > length_before:
            self.students_added.append(True)
        else:
            self.students_added.append(False)

    def roster(self) -> list[str]:
        sorted_students = sorted(self.students, key=lambda o: (o.grade, o.name))
        return [student.name for student in sorted_students]

    def grade(self, grade_number: int) -> list[str]:
        students = [student for student in self.students if student.grade == grade_number]
        sorted_students = sorted(students, key=lambda o: (o.grade, o.name))
        return [student.name for student in sorted_students]

    def added(self) -> list[bool]:
        return self.students_added
