# Task - 11

# my_list = [2, 3, 5, 4, 78, 8]

# count = 0

# for i in my_list:
#     if i % 2 == 0:
#         count += 1

# print(count)

# Task - 12

# my_list = [2, 3, 5, 4, 78, 8]

# for i in my_list:
#     print(i * 2)

# Task - 13

# my_list = [2, 3, 5, 4, 78, 8]

# big_num = my_list[0]

# for i in my_list:
#     if i > big_num:
#         big_num = i

# print(big_num)

# Task - 14

# my_list = [2, 3, 5, 4, 78, 8]

# little_num = my_list[0]

# for i in my_list:
#     if i < little_num:
#         little_num = i

# print(little_num)

# Task - 15

# my_list = [2, 3, 5, 4, 78, 8]

# my_list.reverse()
# print(my_list)

# Task - 16

# my_list = [2, 3, 5, 4, 78, 8]

# zero_list = []

# for i in my_list:
#     if i != 0:
#         zero_list.append(i)

# print(zero_list)

# Task - 17

# my_list = [2, 3, 5, 4, 78, 8]

# for i in my_list:
#     print(i ** 2)

# Task - 18

# my_list = [2, 3, 5, 4, 78, 8, 42, 43, 23, 33]

# count = 0

# for i in my_list:
#     if i > 10:
#         count += i

# print(count)

# Task - 19 

# my_list = [2, 3, 5, 4, 78, 8, 42, 43, 23, 33]

# for i in my_list:
#     if i % 2 != 0:
#         print(i)

# Task - 20 

# my_list = [2, 3, 5, 4, 78, 8, 42, 43, 23, 33]

# for i in my_list:
#     print(i == 7)

# Task - 21

# my_list = [2, 3, 5, 4, 78, 8, 42, 43, 23, 33]
# my_list_2 = [1, 3, 4, 6, 8, 142, 645]

# total_list = []

# my_list.append(my_list_2)
# total_list.append(my_list)

# print(total_list)

# Task - 22

# from random import randint

# n = randint(1, 20)
# steps = 0

# while True:
#     user_input = int(input("Enter a number between 1 - 20 : "))
#     steps += 1

#     if user_input < n:
#         print("Go a little bit upper !")
#     elif user_input > n:
#         print("Go a little bit lower !")
#     else:
#         print("Correct! You find this random number :)")
#         break

# print(steps)

# Task - 23

import random as rn

user_balace = rn.randint(1000, 10000)
print(f"Your balanca : {user_balace}")

user_want = int(input("How many money do you want ( 1000 - 10000 ) : "))
def bank():
    if user_want <= user_balace:
        user_balace -= user_balace
        print(f"You taked : {user_want}")
    else:
        print("You have not enough money ❌")

bank()