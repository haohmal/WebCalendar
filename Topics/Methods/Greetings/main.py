class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        return "Hello, I am {0}!".format(self.name)
        
your_name = input()
you = Person(your_name)
print(you.greet())
