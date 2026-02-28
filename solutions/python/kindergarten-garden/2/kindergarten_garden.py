"""Kindergarten Garden"""

DEFUALT_CLASS = [
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

PLANTS_PER_STUDENT = 2


class Garden:
    def __init__(self, diagram, students=DEFUALT_CLASS):
        rows = diagram.split("\n")
        self.diagram = [list(row) for row in rows]

        # Cups are assigned to students alphabetically
        self.students = sorted(students)

    def plants(self, student: str) -> list:
        """Return a list containing the names of the plants planted by the student."""
        # Find the index of the student in the list of students
        student_index = self.students.index(student)

        plants = []
        for row in self.diagram:
            # Grab their two plants from that row
            plants.append(row[PLANTS_PER_STUDENT * student_index])
            plants.append(row[PLANTS_PER_STUDENT * student_index + 1])

        # Translate the diagram entries into the names of the plants
        plants = [CHARACTER_TO_PLANT[character] for character in plants]

        return plants
