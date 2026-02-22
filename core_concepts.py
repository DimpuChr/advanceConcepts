class Person:

    def __init__(self, name):
        self.name = name
        print("Hello Constructor " + name)

    def get_values(self):
        return self.name


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        #Person.__init__(self, name)
        self.age = age

    def get_age(self):
        return f"name is {self.name} and age is {self.age}"


s = Student('darshan', 36)
print(s.get_age())
