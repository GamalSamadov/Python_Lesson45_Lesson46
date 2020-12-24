# # Task 1
# # площадь прямоугольного треугольника: 0.5 * a * b
# a = int(input('Enter length of first leg: '))
# b = int(input('Enter length of second leg: '))
# area = (1/2) * a * b
# print(f"First leg: {a}, Second leg: {b} Area of this leg: {area}")
#
# # Task 2
# quantity_1 = int(input('Enter quantity of students in the first class: '))
# quantity_2 = int(input('Enter quantity of students in the second class: '))
# quantity_3 = int(input('Enter quantity of students in the third class: '))
# desks_1 = quantity_1/2
# desks_2 = quantity_2/2
# desks_3 = quantity_3/2
# if desks_1 % 2 !=0:
#     desks_1+=0.5
# if desks_2 % 2 !=0:
#     desks_2+=0.5
# if desks_3 % 2 !=0:
#     desks_3+=0.5
# print(desks_1,desks_2,desks_3)
#
# # Task 3
# num_1 = int(input('Enter a number: '))
# num_2 = int(input('Enter a number: '))
# num_3 = int(input('Enter a number: '))
# if num_1 == num_2 and num_2 == num_3:
#     print(3)
# elif num_1 == num_2 and num_2!= num_3 or num_2 == num_3 and num_1 != num_2 or num_1 == num_3 and num_3 != num_2:
#     print(2)
# else:
#     print(0)
#
# Task 4
# leap_number = int(input('Enter a number: '))
# if leap_number%4==0 and leap_number%100!=0 or leap_number%400==0:
#     print('YES')
# else:
#     print('NO')
#
# # Task 5
# number = float(input('Enter a number: '))
# print(str(number%1)[2])
#
# # Task 6
# s=1
# n=int(input('Enter a number'))
# for i in range(1,n+1):
#     s*=i
# print(s)
#
# Task 7
# import math
# leg_1 = int(input('Enter length first leg: '))
# leg_2 = int(input('Enter length first leg: '))
# hypotenuse = math.sqrt((leg_1** 2) + (leg_2**2))
# print(hypotenuse)
#
# # Task 8
# import random
# zero = 0
# N = int(input('Enter a number: '))
# print(N)
# for i in range(N):
#     i = random.randint(0,5)
#     if i == 0:
#         zero+=1
#     print(i)
# print('Zeros: '+str(zero))
#
# # Task 9
# s = str(input('Enter two strings with SPACE: '))
# s = 'ASD DSA'
# w = s.find(' ')
# print(f'{s[w:]} {s[:w]}')
#
# # Task 10
# s = str('Folbin Folbin Folbin')
# if s.count('F') == 1:
#     print(-1)
# elif s.count('F') == 0:
#     print(-2)
# elif s.count('F')>1:
#     print(s.find('F',+1))
