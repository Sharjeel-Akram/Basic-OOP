def Student(Name,ID,limit):
    name = Name
    Roll_No = ID

    print('name of student is: ', name, '\n' 'roll number of student is: ',Roll_No)

    Marks = []
    Courses = []
    print(Courses)
    
    for i in range(limit):
        Courses.append(input('enter your course: '))
        Marks.append((input('enter your marks: ')))
    print(Courses, Marks)
    index = 0
    for i in range(len(Marks)):
        if Marks[i] > Marks[0]:
            index = i
    print('highest marks in course of student: ', Courses[index], '\n', 'highest marks: ', Marks[index] )




finish = 0
while finish == 0:
    Courses_limit = int(input('enter your courses: '))
    Student_name = input('enter your name: ')
    Student_ID = int(input('enter your ID: '))

    Student(Student_name, Student_ID, Courses_limit)