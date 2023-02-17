from classes.school import School 
from classes.staff import Staff
from classes.student import Student

school = School('Ridgemont High') 

print(school.name)
print(school.students)
print(school.staffs)

mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")
print(mode)


if mode =='1':
    print(Student.student_list)
elif mode =='2':
    student_id=input('Input ID')
    for student in Student.student_list:
        if student.id==student_id:
            print(student)
elif mode =='5':
    exit()

print(mode)
