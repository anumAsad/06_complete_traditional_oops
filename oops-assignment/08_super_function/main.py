# parent class
class Person:
    def __init__(self, name):
        self.name = name

# child class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}")

# creating object
if __name__ == "__main__":
    teacher = Teacher("Anum", "Mathematics")
    teacher.display()
