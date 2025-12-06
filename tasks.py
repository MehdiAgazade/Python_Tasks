# def roman_nums(num):
#     nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80 ,70 ,60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#     symbols = ["M", "CM", "DCCC", "DCC", "DC", "D", "CD", "CCC", "CC", "C", "XC", "LXXX", "LXX", "LX", "L", "XL", "XXX", "XX", "X", "IX", "VIII", "VII", "VI", "V", "IV", "III", "II", "I"]

#     roman_num = ""

#     i = 0

#     while num > 0:
#         while num >= nums[i]:
#             roman_num += symbols[i]
#             num -= nums[i]
#         i += 1
#     return roman_num

# user_date = input("Enter your birth date ( dd.mm.yyyy ) : ")

# day, month, year = user_date.split(".")
# day, month, year = int(day), int(month), int(year)


# day = roman_nums(day)
# month = roman_nums(month)
# year = roman_nums(year)

# print(f"{day}.{month}.{year}")

# --------------------------------------------

# n = int(input("Enter a number : "))
# steps = 0

# while n >= 0:

#     if n % 2 == 0:
#         n = n / 2
#         steps += 1
#     elif n % 2 != 0:
#         n = n - 1
#         steps += 1

# print(steps)

# user1 = int(input("Enter first number : "))
# user2 = int(input("Enter second number : "))

# def sum():
#     print(user1 + user2

# sum()

# user_input = int(input("Enter a number : "))

# def num():
#     if user_input % 2 == 0:
#         print("The number you entered is an even number :)")
#     else:
#         print("The number entered is not an even number. Try again :(")

# num()

# user_want = input("What do you want to buy ( Cap, T-Shirt, Trousers) : ")

# balance = 200

# storeage = {
#     "Cap": 5,
#     "T-Shirt": 20,
#     "Trousers": 30
# }

# price = {
#     "Cap": 4,
#     "T-Shirt": 25,
#     "Trousers": 52
# }

# if user_want in storeage:
#     user_number = int(input("How many do you want : "))
# elif user_want 
# elif user_number > storeage["Cap"] or storeage["T-Shirt"] or storeage["Trousers"]:
#     print("We haven't enough you want !")
# else:
#     print("The clothes you entered is not aviable!")