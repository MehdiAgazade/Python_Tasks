our_code = ["bob", "qwerty", "john", "pass"]

steps = 0

while True:
    user_input = input("Enter a code : ").lower()
    steps += 1

    if user_input in our_code:
        print("You signed up !")
        print("Steps :", steps)
        break
    else:
        print("Try again !!!")

    # elif user_input == "qwerty":
    #     print("You signed up !")
    # elif user_input == "john":
    #     print("You signed up !")
    # elif user_input == "pass":
    #     print("You signed up !")
    # else:
    #     print("Try again !!!")








    # if user_input == "bob" or user_input == "" or user_input == "john" or user_input == "pass":
    #     
    # else:
    #     print("Try again !!!")
    #     steps += 1