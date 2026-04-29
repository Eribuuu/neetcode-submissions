class LinkedList:
    
    class node:
        def __init__(self, val = None, nxt = None):
            self.val = val
            self.next = nxt
    
    def __init__(self):
        self.head = None
        self.size = 0

    
    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        else:
            currNode = self.head
            for i in range(index):
                currNode = currNode.next
            return currNode.val

    def insertHead(self, val: int) -> None:
        if self.head == None:
            self.head = LinkedList.node(val, None)
        else:
            newNode = LinkedList.node(val, self.head)
            self.head = newNode
        self.size += 1

    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.head = LinkedList.node(val, None)
        else:
            currNode = self.head
            while currNode.next != None:
                currNode = currNode.next
            newNode = LinkedList.node(val, None)
            currNode.next = newNode
        self.size += 1
        
    def remove(self, index: int) -> bool:
        if index >= self.size or index < 0:
            return False
        else:
            self.size -= 1
            if index == 0:
                self.head = self.head.next
                return True
            else:
                currNode = self.head
                for i in range(index - 1):
                    currNode = currNode.next
                currNode.next = currNode.next.next
                return True


    def getValues(self) -> List[int]:
        values = []
        currNode = self.head
        while currNode != None:
            values.append(currNode.val)
            currNode = currNode.next
        return values