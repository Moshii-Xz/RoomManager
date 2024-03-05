import numpy as np
from abc import ABC, abstractmethod
from Room import Room

class Room(Room, ABC):
    def SellSeat(self, letter:str, number:int):  # validate that a sold seat is not sold again
        if letter in self.rowLetters and self.initialSeat <= number <= self.numberOfSeatsPerRow:
            row = self.rowLetters.index(letter)
            column = number - 1
            if self.seats[row][column] == "X" and self.seats[row][column] != "O":
                self.seats[row][column] = "O"
                print("\033[1;32mThe sale was successful!\033[0;m")
            else:
                print("\033[1;31mThe seat is already sold!\033[0;m")
        else:
            print("\033[1;31mThe letter or number is invalid!\033[0;m")

    def CalculateSoldSeatsQuantity(self):
        soldSeats = filter(lambda seat: seat == "O", (self.seats[row][column] for row in range(self.numberOfRows) for column in range(self.numberOfSeatsPerRow)))
        soldSeatsCount = len(list(soldSeats))
        return soldSeatsCount


    def CalculateAvailableSeatsQuantity(self):
        soldSeatsCount = self.CalculateSoldSeatsQuantity()
        availableSeatsCount = self.totalNumberOfSeats - soldSeatsCount
        return availableSeatsCount

    def CalculateRevenue(self):
        totalRevenue = 0
        lowPriceSeat = 5000
        mediumPriceSeat = 15000
        highPriceSeat = 20000
        centralRow = (self.numberOfSeatsPerRow - 1) / 2
        for row in range(0, self.numberOfRows):
            for column in range(0, self.numberOfSeatsPerRow):
                if self.seats[row][column] == "O":
                    if (row == column and row >= centralRow) or (row + column == self.numberOfSeatsPerRow - 1 and row >= centralRow):
                        totalRevenue = totalRevenue + mediumPriceSeat
                    elif (row + column > self.numberOfSeatsPerRow  - 1 and row > column):
                        totalRevenue = totalRevenue + highPriceSeat
                    else:
                        totalRevenue = totalRevenue + lowPriceSeat
        return totalRevenue
