class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arraylist = [None] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        if i < 0 or i > self.size:
            raise IndexError("Index out of bounds")
        return self.arraylist[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i > self.size:
            raise IndexError("Index out of bounds")
        self.arraylist[i] = n

    def pushback(self, n: int) -> None:
        if self.size == len(self.arraylist):
            self.resize()
        self.arraylist[self.size] = n
        self.size += 1
            
    def popback(self) -> int:
        element = self.arraylist[self.size - 1]
        self.arraylist[self.size - 1] = None
        self.size -= 1
        return element

    def resize(self) -> None:
        new_capacity = max(1, len(self.arraylist) * 2)
        tempArray = [None] * new_capacity 
        for i in range(self.size):            
            tempArray[i] = self.arraylist[i]
        self.arraylist = tempArray

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.arraylist)