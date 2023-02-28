#python conditionals
def is_positive():

    x = int(input("Enter a random number: "))

    if(x < 0):
        print("The number you entered is negative: ", x)
    elif(x > 0):
        print("You entered a positive number: ", x)
    elif(x == 0):
        print("You entered zero")
    else:
        print("You did not enter a number")

is_positive()
