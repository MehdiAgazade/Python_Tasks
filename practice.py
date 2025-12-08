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
