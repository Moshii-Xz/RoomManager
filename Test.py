from BusinessLogic import Room
from GetInput import *
from FunctionMix import *
cineCostaRoom = Room(AskName(), AskRoomDimensions())

centralRow = (cineCostaRoom.numberOfSeatsPerRow - 1) / 2

while True:
    print("--------------------------------------------------")
    print("\033[1;3;30;40mWelcome to the CAJAMAG theater sales system\033[0;m")
    print("\033[1;3;37;40m 1. Sell seat                           \033[0;m")
    print("\033[1;3;37;40m 2. Calculate number of seats sold   \033[0;m")
    print("\033[1;3;37;40m 3. Calculate number of available seats\033[0;m")
    print("\033[1;3;37;40m 4. Calculate revenue obtained              \033[0;m")
    print("\033[1;3;37;40m 5. Print seats                        \033[0;m")
    print("\033[1;3;31;40m 6. Exit                                    \033[0;m")
    print("--------------------------------------------------")
    option = (input("\033[1;36mEnter an option: \033[0;m"))
    IsInteger(option)
    if option == "1":
        print("-----------------")
        print("\033[1;36mSell seat\033[0;m")
        print("-----------------")
        print("Row letters: ", cineCostaRoom.rowLetters)
        print("Number of seats per row: ", cineCostaRoom.numberOfSeatsPerRow)
        cineCostaRoom.SellSeat(AskLetter(), AskNumber())
    elif option == "2":
        print("-----------------")
        print("\033[1;36mCalculate number of seats sold\033[0;m")
        print("-----------------")
        print("Number of seats sold: ", cineCostaRoom.CalculateSoldSeatsQuantity())
    elif option == "3":
        print("-----------------")
        print("\033[1;36mCalculate number of available seats\033[0;m")
        print("-----------------")
        print("Number of available seats: ", cineCostaRoom.CalculateAvailableSeatsQuantity())
    elif option == "4":
        print("-----------------")
        print("\033[1;36mCalculate revenue obtained\033[0;m")
        print("-----------------")
        print("Revenue obtained: ", cineCostaRoom.CalculateRevenue())
    elif option == "5":
        print("-----------------")
        print("\033[1;36mPrint seats\033[0;m")
        print("-----------------")
        print("Seats in the room", cineCostaRoom.name)
        print(" ", end="")
        for number in range(1, cineCostaRoom.numberOfSeatsPerRow+1):
            print(" ", number, end="")
        print()
        for row in range(0, cineCostaRoom.numberOfRows):
            print(cineCostaRoom.rowLetters[row], end="")
            for column in range(0, cineCostaRoom.numberOfSeatsPerRow):
                if cineCostaRoom.seats[row][column] == "X":
                    if (row == column and row >= centralRow) or (row + column == cineCostaRoom.numberOfSeatsPerRow -1 and row >= centralRow):
                        print("\033[1;32m", cineCostaRoom.seats[row][column], "\033[0;m", end="")
                    elif (row + column > cineCostaRoom.numberOfSeatsPerRow  -1 and row > column):
                        print("\033[1;30m", cineCostaRoom.seats[row][column], "\033[0;m", end="")
                    else:
                        print("\033[1;33m", cineCostaRoom.seats[row][column], end=" ")
                else:
                    print("\033[1;31m", cineCostaRoom.seats[row][column], end=" ")
            print("\033[0;m")
        print("Remember that available seats are marked with an ""X"" and sold seats with an ""O"" in red")
    elif option == "6":
        print("\033[1;32mThank you for using the CINECOSTA sales system\033[0;m")
        break
    else:
        print("\033[1;31mInvalid option\033[0;m")