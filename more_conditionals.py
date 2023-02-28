#more conditionals
def strlen(str):
    if(type(str) == int or type(str) == float):
        print("The value entered is not a string")
    else:
        print(len(str))

strlen(10.322)
