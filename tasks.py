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

n = int(input("Enter a number : "))
steps = 0

while n >= 0:

    if n % 2 == 0:
        n = n / 2
        steps += 1
    elif n % 2 != 0:
        n = n - 1
        steps += 1

print(steps)