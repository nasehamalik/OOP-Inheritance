class Adult():
    # Create a constructor to display the name, age, eye_colour and hair_colour of the adult
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    # Create a function to print an individual who can drive
    def can_drive(self):
        print(self.name, "is old enough to drive")

class Child(Adult):
    # Create a constructor to display the attributes of the child and use the super function to follow the same method
    def __init__(self, name, age, eye_colour, hair_colour):
        super().__init__(name, age, eye_colour, hair_colour)

    # Create a overide for the can_drive function, stating the individual is too young to drive
    def can_drive(self):
        print(self.name, "cannot drive as they are too young")
 
# Request the user to enter their atributes
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
eye_colour = input("Please enter your eye colour: ")
hair_colour = input("Please enter your hair colour: ")

attributes = None
 # Identify if the individual is an adult or an adult
if age >= 18:
    attributes = Adult(name, age, eye_colour, hair_colour)
    attributes.can_drive()
else:  
    attributes = Child(name, age, eye_colour, hair_colour)
    attributes.can_drive()