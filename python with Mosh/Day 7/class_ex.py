class Person:
    def __init__(self, name):
        self.name = name
        
    
    def talk(self):
        return f"My name is {self.name} and I am learning to code"

person1 = Person("Nitesh")
print(person1.talk())