from abc import ABC, abstractmethod
import numpy as np

class Room(ABC):
    def __init__(self, name, numberOfRows):
        self.name = name
        self.numberOfRows = numberOfRows
        self.numberOfSeatsPerRow = self.numberOfRows
        self.initialSeat = 1
        self.seats = np.full((self.numberOfRows, self.numberOfSeatsPerRow), "X")
        self.totalNumberOfSeats = self.numberOfSeatsPerRow * self.numberOfRows
        allLetters = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
        self.rowLetters = allLetters[:self.numberOfRows]

    @abstractmethod
    def SellSeat(self, letter:str, number:int):
        pass

    @abstractmethod
    def CalculateSoldSeatsQuantity(self):
        pass

    @abstractmethod
    def CalculateAvailableSeatsQuantity(self):
        pass

    @abstractmethod
    def CalculateRevenue(self):
        pass
