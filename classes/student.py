from .person import Person
import os
import csv


class Student(Person): 
    student_list=[]
    total_students=0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id=kwargs.get('school_id')
        
        Student.total_students+=1
    def __str__(self):
        return f"{self.name.upper()} \n ______________\nage: {self.age}\nid: {self.id}"
    

file_folder='/Users/yenpham/Tango/curriculum/week-02/day3/data'
student_fpath=os.path.join(file_folder,'students.csv')

with open(student_fpath,'r') as student_f:
    student_csv=csv.DictReader(student_f)
    for line in student_csv:
        Student.student_list.append(Student(**line))




