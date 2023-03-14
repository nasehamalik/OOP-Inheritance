class Course():
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office = "Cape Town"
    
     # Create a function called contact details 
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

     # Create a subclass of the Course class named OOPCourse
class OOPCourse(Course):
     # Create a constructor to identify the course description, trainer name and ID
    def __init__(self, description, trainer, ID):
        self.description = description
        self.trainer = trainer
        self.ID = ID

        description = "OOP Fundamentals"
        trainer = "Mr Anon A. Mouse"
        ID = "#12345"

     # Create a function called trainer details including the course description and name of the trainer
    def trainer_details(self): 
        print("The course description is", self.description)
        print("The name of the trainer is", self.trainer)
     # Create a function to display the course ID number
    def show_course_id(self):
        print("The ID number of the course is", self.ID)

  # Create an object which calls the functions; contact_details, trainer_details and show_course_id
course_1 = OOPCourse("description", "trainer", "ID")
course_1.contact_details
course_1.trainer_details
course_1.show_course_id