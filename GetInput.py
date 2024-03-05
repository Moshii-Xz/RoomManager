from FunctionMix  import *

def AskName() -> str:
    while True:
            name = input("Please enter the name of the room: ")
            if len(name) != 0:
                break
            else:
                print("The name is not valid! The name cannot contain spaces or numbers!")
    return name

def AskLetter() -> str:
    letters =("A","B","C","D","E")
    while True:
        letter = input("Enter the seat letter: ").upper()
        if letter in letters:
            break
        else:
            print("The letter is not valid!")
    return letter

def AskNumber():
    while True:
        number = input("Enter the seat number: ")
        if IsInteger(number):
            number = int(number)
            if 1 <= number <= 10:
                break
            else:
                print("The number must be greater than or equal to 1 and less than or equal to 10!")
        else:
            print("The number must be an integer!")
    return number

def AskRoomDimensions() -> int:
    while True:
        dimensions = input("Enter the room dimensions: ")
        if IsInteger(dimensions):
            dimensions = int(dimensions)
            if 3 <= dimensions <= 27:
                break
            else:
                print("The number must be greater than or equal to 3 and less than or equal to 27!")
        else:
            print("The number must be an integer!")
    return dimensions
