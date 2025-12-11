# Task - 1

# my_list = [1, 2, 3, 4, 5]
# print(my_list)

# Task - 2

# my_list = ["salam", "necesen", "ne var", "ne yox"]
# print(my_list[0])

# Task - 3

# my_list = [1, 21.23, "salam", True, "necesen"]
# print(my_list[4])

# Task - 4

# my_list = [1, 23, 43, 65, 45]
# my_list[1] = 100
# print(my_list)

# Task - 5

# my_list = ["salam", "bir", "iki", "uc", "necesen", "hello"]
# my_list.append("men")
# print(my_list)

# Task - 6

# my_list = ["salam", "bir", "iki", "uc", "necesen", "hello", "men"]
# my_list.pop()
# print(my_list)

# Task - 7

# Basaaa dusmeddimmmm helppppppppppppppppppp

# Task - 8

# my_list = ["salam", "bir", "iki", "uc", "necesen", "hello"]
# print(my_list)
# print(len(my_list))

# Task - 9


# Task - 10 

# my_list = ["qarpuz", "alca", "ciyelek", "banan", "papaya", "mango"]
# print(my_list)

# Task - 11

dict = ["dog", "cat", "bee", "bird", "horse", "snake", "spider"]

user_choose = input("Write a animal name : ").lower()
steps = 0


while True:
    if user_choose == "dog":
        print("Hav hav hav")
        steps += 1
        break
    elif user_choose == "cat":
        print("Miav miav miav")
        steps += 1
        break
    elif user_choose == "bee":
        print("Vizz vizz vizz")
        steps += 1
        break
    elif user_choose == "bird":
        print("Cik cik cik")
        steps += 1
        break
    elif user_choose == "horse":
        print("I-ihiiiii")  
        steps += 1
        break
    elif user_choose == "snake":
        print("Siii Siii Siii")
        steps += 1
        break
    elif user_choose == "spider":
        print("Cigss cigss cigss")
        steps += 1
        break
    else:
        print("The animal name you writed is not enable. Try again !!!")
