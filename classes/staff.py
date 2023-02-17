from .person import Person
import csv
import os

class Staff(Person):
    staff_list=[]
    total_staff=0
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.employee_id=kwargs.get('employee_id')
        Staff.staff_list.append(self)
        Staff.total_staff+=1

    def __str__(self):
        return f'{self.name}'

file_folder='/Users/yenpham/Tango/curriculum/week-02/day3/data'
staff_fpath=os.path.join(file_folder,'staff.csv')

with open(staff_fpath,'r') as staff_file:
    staff_csv=csv.DictReader(staff_file)
    for line in staff_csv:
        Staff(**line)
# print(Staff.total_staff)
# print(Staff.staff_list)
# for i in Staff.staff_list:
#     print(i)


