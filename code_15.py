class Student:
    def __init__(self):
        self.name = "James"
        self.grade = 90
        
    def get_grade(self):
        return self.grade
    
    
    # str() is used for creating output for end user while repr() is mainly used for debugging and development. 
    # repr’s goal is to be unambiguous and str’s is to be readable.
    # Usually you want to implement the str() method
    
    def __str__(self):
        return f"Person: {self.name}, Grade: {self.grade}"
    
        
student = Student()

print(student.name)

print(student.get_grade())

print(student)