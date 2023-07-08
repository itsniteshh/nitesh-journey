class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        return f"My name is {self.name} and age is {self.age}"

person1 = Person("Nitesh Jha", 28)
print(person1.name)
