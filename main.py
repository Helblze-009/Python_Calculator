# Function to add two numbers

def addition(x, y):
    return x+y

# Function to subttract two numbers


def subtraction(x, y):
    return x - y

# Function to multiply two numbers


def multiplication(x, y):
    return x*y

# Function to add two numbers


def division(x, y):
    return x/y


print("Hi, I am a Calculator.")
print("press 1 for addition"),
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")

while(True):
    # taking input from user
    user_input = input("Enter Your choice (1 , 2 , 3 , 4) :")

    if user_input in ("1", "2", "3", "4"):
        num1 = int(input("Enter Your first number:"))
        num2 = int(input("Enter Your second number:"))

        if (user_input == "1"):
            # Faulty calculator
            #  if(num1 == 56 and num2 == 9):
            #      print("Your result is 77")

            #  else:
            #      print("Your result is ", multiplication(num1, num2))
            print("Your result is ", addition(num1, num2))
        elif (user_input == "2"):
            print("Your result is ", subtraction(num1, num2))
        elif (user_input == "3"):

            # Faulty calculator
            # if(num1 == 45 and num2 == 3):
            #     print("Your result is 555")

            # else:
            #     print("Your result is ", multiplication(num1, num2))
            print("Your result is ", multiplication(num1, num2))
        elif (user_input == "4"):
            # Faulty calculator
            # if(num1 == 56 and num2 == 6):
            #     print("Your result is 4")

            # else:
            #     print("Your result is ", multiplication(num1, num2))
            print("Your result is ", division(num1, num2))
        else:
            print("Invalid Input")

    # Taking another input if user wants

    user_input2 = input("Want to make another calculation? (yes/no?) :")
    if user_input2 == "yes":
        print("OK , Here we go again.")

    elif user_input2 == "no":
        print("Thank You")
        break
    else:
        print("Invalid Input.")
