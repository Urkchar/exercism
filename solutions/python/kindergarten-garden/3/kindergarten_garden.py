"""Kindergarten Garden"""

DEFAULT_STUDENTS = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry"
]

# Translate a diagram entry into the name of the plant
CHARACTER_TO_PLANT = {
    "G": "Grass",
    "C": "Clover",
    "R": "Radishes",
    "V": "Violets"
}

COLUMNS_PER_STUDENT = 2


class Garden:
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        rows = diagram.split("\n")
        diagram_characters = [list(row) for row in rows]
        self.diagram = [[CHARACTER_TO_PLANT[character] for character in row] for row in rows]

        # Cups are assigned to students alphabetically
        self.students = sorted(students)

    def plants(self, student: str) -> list:
        """Return a list containing the names of the plants planted by the student."""
        # Find the index of the student in the list of students
        student_index = self.students.index(student)

        plants = []
        for row in self.diagram:
            # Grab their two plants from that row
            plants.append(row[COLUMNS_PER_STUDENT * student_index])
            plants.append(row[COLUMNS_PER_STUDENT * student_index + 1])

        return plants
