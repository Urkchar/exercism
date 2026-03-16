"""Module providing classes representing students and schools."""


class Student:
    """Class representing a student.
    Students are considered equal if they have the same name.
    """
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
    """Class representing a school.
    Supported operations:
    Add a student to the school.
    Check the current roster.
    Check which students are in a given grade.
    Check which student-add operations were successful.
    """
    def __init__(self):
        self.students = set()
        self.students_added = []

    def add_student(self, name: str, grade: int):
        """Attempt to add a student to the roster."""
        student = Student(name, grade)
        length_before = len(self.students)
        self.students.update({student})
        length_after = len(self.students)

        if length_after > length_before:
            self.students_added.append(True)
        else:
            self.students_added.append(False)

    def roster(self) -> list[str]:
        """Return the names of the students in the roster, sorted by grade and 
        then by name.
        """
        sorted_students = sorted(self.students, key=lambda o: (o.grade, o.name))
        return [student.name for student in sorted_students]

    def grade(self, grade_number: int) -> list[str]:
        """Return the names of the students in a given grade, sorted by grade 
        and then by name.
        """
        students = [student for student in self.students if student.grade == grade_number]
        sorted_students = sorted(students, key=lambda o: (o.grade, o.name))
        return [student.name for student in sorted_students]

    def added(self) -> list[bool]:
        """Return the results of all attempted student-add operations."""
        return self.students_added
