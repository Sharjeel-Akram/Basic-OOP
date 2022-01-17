limit = int(input("enter your limit: "))
count_one = 0
count_two = 0
count_three = 0
count_four = 0
count_five = 0
count_six = 0
count_seven = 0
count_eight = 0
count_nine = 0
count_ten = 0

List = []
for i in range(limit):
    number = int(input('enter your number: '))
    List.append(number)
    if number < 0 or number > 10:
        print('invalid number')
        break

for i in List:
    if i == 1:
        count_one += 1
    if i == 2:
        count_two += 1
    if i == 3:
        count_three += 1
    if i == 4:
        count_four += 1
    if i == 5:
        count_five += 1
    if i == 6:
        count_six += 1
    if i == 7:
        count_seven += 1
    if i == 8:
        count_eight += 1
    if i == 9:
        count_nine += 1
    if i == 10:
        count_ten += 1

if count_one > 1:
    print(count_one * '*')
if count_two > 1:
    print(count_two * '*')
if count_three > 1:
    print(count_three * '*')
if count_four > 1:
    print(count_four * '*')
if count_five > 1:
    print(count_five * '*')
if count_six > 1:
    print(count_six * '*')
if count_seven > 1:
    print(count_seven * '*')
if count_eight > 1:
    print(count_eight * '*')
if count_nine > 1:
    print(count_nine * '*')
if count_ten > 1:
    print(count_ten * '*')