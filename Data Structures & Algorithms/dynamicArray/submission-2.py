class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.numElement = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.numElement >= len(self.array):
            self.resize()
        self.array[self.numElement] = n
        self.numElement += 1

    def popback(self) -> int:
        element = self.array[self.numElement - 1]
        self.numElement -= 1
        return element

    def resize(self) -> None:
        newArray = [0] * (2 * len(self.array))
        for i in range(len(self.array)):
            newArray[i] = self.array[i]
        self.array = newArray

    def getSize(self) -> int:
        return self.numElement
    
    def getCapacity(self) -> int:
        return len(self.array)