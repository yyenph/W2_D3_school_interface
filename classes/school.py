
from .student import Student
from .staff import Staff
class School:

    def __init__(self,name):
        self.name=name
        self.staffs=Staff.staff_list
        self.students=Student.student_list
        


# school = School('Ridgemont High') 
# print(school.students)


        
