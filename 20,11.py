##import random
##students = ["Гарри Поттер","Драко малфой","Гермиона Греджер","Рон Уизли",
##            "Полумна Лавгул","Джини Уизли"]
##gryffindor = []
##slytherin = []
##hufflepuff = []
##while len(students) != 0:
##    student = random.choice(students)
##    choise = random.randint(1,300)
##    if choise <= 100:
##        gryffindor.append(student)
##        print(student + " Отправляется в Гриффиндор")
##    elif choise <= 200:
##        slytherin.append(student)
##        print(student + " Отправляется в Слизерин")
##    else:
##        hufflepuff.append(student)
##        print(student + " Отправляется в Хафлпаф")
##    students.remove(student)
##print(students, "В списке учеников никого не осталось")


###Задача 2
###Даны списки:
###3a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
###b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
###Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
##a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
##b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
##o = []
##for i in range(len(a)):
##    contains = 0
##    num = a[0]
##    for i in range(len(b)):
##        if num == b[i]:
##            contains = 1
##
##            break
##    if contains == 1:
##        o.append(num)
##        a.remove(num)
##print(o)
   
    
###Задача 3
##import random
##lst = []
##n = 10
##for i in range(n):
##    lst. append(random.randint(0,10))
##print(lst)
##k = 0
##for i in range(n):
##    if lst[i] % 2 == 0:
##        k = k + lst[i]
##print(k)

#Задача 4
import random
lst = []
n = 10
for i in range(n):
    lst. append(random.randint(-30,-5))
print(lst)
k = 0
for i in range(n):
    if lst[i] % 3 == 0:
        k = k + lst[i]
print(k)












    
