Student1 = []
Student2 = []
Student3 = []
Student4 = []
Student5 = []
subject=['oop','dld','gb','itp','isl']
for i in range(5):
    for j in range(1):
        numbers1 = int(input('enter marks of student1: '))
        Student1.append(numbers1)
    for k in range(1):
        numbers2 = int(input('enter marks of student2: '))
        Student2.append(numbers2)
    for l in range(1):
        numbers3 = int(input('enter marks of student3: '))
        Student3.append(numbers3)
    for m in range(1):
        numbers4 = int(input('enter marks of student4: '))
        Student4.append(numbers4)
    for n in range(1):
        numbers5 = int(input('enter marks of student5: '))
        Student5.append(numbers5)
print(subject)
print(Student1)
max1=0
index1=0

for i in range(len(Student1)):
    if Student1[0] < Student1[i]:
        max1=Student1[i]
        index1=i
    else:
        max1=max1
print(subject[index1])

print(Student2)

max2 = 0
index2 = 0

for i in range(len(Student2)):
    if Student2[0] < Student2[i]:
        max2 = Student2[i]
        index2 = i
    else:
        max2 = max2
print(subject[index2])

print(Student3)

max3 = 0
index3 = 0

for i in range(len(Student3)):
    if Student3[0] < Student3[i]:
        max3 = Student3[i]
        index3 = i
    else:
        max3 = max3
print(subject[index3])
print(Student4)

max4 = 0
index4 = 0

for i in range(len(Student4)):
    if Student4[0] < Student4[i]:
        max4 = Student4[i]
        index4 = i
    else:
        max4 = max4
print(subject[index4])

print(Student5)

max5 = 0
index5 = 0

for i in range(len(Student5)):
    if Student5[0] < Student5[i]:
        max5 = Student5[i]
        index5 = i
    else:
        max5 = max5
print(subject[index5])
