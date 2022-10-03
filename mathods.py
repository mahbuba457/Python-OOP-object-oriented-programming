class student:
    roll = ""
    gpa = ""

    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll:{self.roll},gpa:{self.gpa}")


karim = student()
karim.set_value(102, 3.75)
karim.display()
