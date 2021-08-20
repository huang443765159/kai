import random

number_list1 = []
for x in range(10):
    number_list1.append(random.randint(1, 100))
print(number_list1)

number_list2 = []
for m in range(10):
    number_list2.append(random.randint(1, 100))
print(number_list2)

number_list3 = []
for z in range(10):
    number_list3.append((random.randint(1, 100)))
print(number_list3)

for number1 in number_list1:
    for number2 in number_list2:
        for number3 in number_list3:
            if number1 + number2 + number3 == 100:
                print(number1, number2, number3)

