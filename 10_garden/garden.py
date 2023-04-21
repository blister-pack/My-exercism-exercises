class Garden:
    student_list = [
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
        "Larry",
    ]

    plant_keys = {"V": "Violets", "R": "Radishes", "C": "Clover", "G": "Grass"}

    def __init__(
        self, diagram, students=student_list
    ):  #  why does this accept studend_list
        #  and not Garden.student_list?????
        self.students = sorted(students)
        rows = diagram.split("\n")
        self.row1 = rows[0]
        self.row2 = rows[1]

    def plants(self, student_name):
        # should take student name and return a list of
        # plant names belonging to that student
        plant_list_by_student = []
        for index, i in enumerate(range(0, len(self.row1), 2)):
            plant_list_by_student.append(self.row1[i : i + 2])
            plant_list_by_student[index] += self.row2[i : i + 2]

        student_index = self.students.index(student_name)
        plants_of_student = plant_list_by_student[student_index]
        #-----------------------------------
        # now we need to get the plant names
        #-----------------------------------
        plants_with_names = []
        for plant in plants_of_student:
            plants_with_names.append(Garden.plant_keys[plant])
        return plants_with_names
# --------------------------------------------------------------------

garden1 = Garden("VRCC\nVCGG", ["Valorie", "Raven"])
garden1.plants("Valorie")
garden2 = Garden("RC\nGG")
