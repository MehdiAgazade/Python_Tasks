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

# dict = {
#     "dog": "hav hav hav",
#     "cat": "miav miav miav",
#     "bee": "vizz vizz vizz",
#     "bird": "cik cik cik",
#     "horse": "I-ihiiiii",
#     "snake": "Ss sss sss",
#     "spider": "Cigss cigss cigss"
# }

# user_choose = input("Enter a animal name : ").lower()
# steps = 0

# while True:
#     if user_choose == "dog":
#         print("Hav hav hav")
#         steps += 1
#         break
#     elif user_choose == "cat":
#         print("Miav miav miav")
#         steps += 1
#         break
#     elif user_choose == "bee":
#         print("Vizz vizz vizz")
#         steps += 1
#         break
#     elif user_choose == "bird":
#         print("Cik cik cik")
#         steps += 1
#         break
#     elif user_choose == "horse":
#         print("I-ihiiiii")  
#         steps += 1
#         break
#     elif user_choose == "snake":
#         print("Sss Sss Sss")
#         steps += 1
#         break
#     elif user_choose == "spider":
#         print("Cigss cigss cigss")
#         steps += 1
#         break
#     else:
#         print("The animal name you writed is not enable. Try again !!!")

# def user():
#     while True:
#         user_input = input("Enter a number : ")

#         if user_input.isdigit():
#             count = 0

#             for i in user_input:
#                 count += int(i) ** 2
                
#             print(count)
#             break
#         else:
#             print("Try again !!!")

# user()

# Task - 12

# try:
#     user1 = int(input("Enter the first number : "))
#     user2 = int(input("Enter the second number : "))

#     result = user1 / user2
#     print(result)
# except ZeroDivisionError:
#     print("Error: Cannot divide by 0! Please try again")

# Task - 13

# try:
#     user_input = input("Enter a word : ")
#     int(user_input)
#     print("The input you entered is not a word. Try again !!!")
# except ValueError:
#     print("It's True. Perfect")
    
# Task - 14

# try:
#     f = open("Write.txt", "w")
#     f.write("Salam Mellim")
#     f = open("Write.txt", "r")
#     print(f.read())
# except Exception as r:
#     print("Error 404", r)
# finally:
#     f.close()
#     print("It's over")

# Task - 15

# key_dict = {
#     "key1" : 2010,
#     "key2" : 2015,
#     "key3" : 1031,
#     "key4" : 2231
# }

# try:
#     user_input = input("Enter the true key for the value : ").lower()
#     print(key_dict[user_input])
# except KeyError:
#     print("You entered the False key. Try again !!!")

class Product:
    def __init__(self, name, count):
        self.product_name = name
        self.product_count = count

products = [Product("Iphone", 10), Product("Samsung", 20)]

def add_product():
    new_product_name = input("Mehsulun adını daxil edin: ")
    new_product_count = int(input("Mehsulun sayını daxil edin: "))
    new_product = Product(new_product_name, new_product_count)
    for i in range(0, len(products)):
        if products[i].product_name == new_product_name:
            products[i].product_count += new_product_count
        # else:
        #     print(new_product)
        
def show_all_products():
    for i in range(0, len(products)):
        print(f"{products[i].product_name}  -->  {products[i].product_count}")

def delete_product():
    name = input("Silmek istediyiniz mehsulun adini daxil edin: ")
    new_deleted_product_count = int(input("Silmek istediyiniz mehsulun sayını daxil edin: "))
    # new_deleted_product = Product(name, new_deleted_product_count)
    for product in products:
        if product.product_name == name:
            if product.product_count >= new_deleted_product_count:
                product.product_count -= new_deleted_product_count
                print("Mehsul ugurla silindi")
            else:
                print("Kifayet qeder mehsul yoxdur") 

def show_deleted_all_produts():
    for i in range(0, len(products)):
        print(f"{products[i].name} --> {products[i].product_count}")

def menu():
    while True:
        print("1. Mehsul elave etmek\n2. Butun mehsullari gostermek\n3. Mehsul silmek\n4. Cixis etmek")
        selection = int(input("\nZehmet olmasa secim edin: "))

        match selection:
            case 1:
                add_product()
            case 2:
                show_all_products()
            case 3:
                delete_product()
            case 4: 
                print("\nCixis edildi")
                break
            case _:
                print("Yalnis daxil etdiniz. Zehmet olmasa yeniden daxil edin")

menu()