class Student: #the actual student will be an object. This is a class

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name #The name of the student object will be equal to the name we passed in
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False