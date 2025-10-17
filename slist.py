
class SList:
    class SListNode:
        def __init__ (self, value = None):
            self.value = value
            self.next = None

    def __init__ (self):
        self._head = None
        self._size = 0
        self._iterator = 0

    '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
    def insert(self, value):
        newNode = self.SListNode(value)
        currentNode = self.SListNode()
        if self._head != None:
            currentNode.next = self._head
            while True:
                if not currentNode.next:
                    currentNode.next = newNode
                    print('pushback')
                    break
                else:
                    if self._head.value > value:
                        newNode.next = self._head
                        self._head = newNode
                        print('new head')
                    else:
                        if value > currentNode.next.value:
                            currentNode = currentNode.next
                        else:
                            newNode.next = currentNode.next
                            currentNode.next = newNode
                            break
        else:
            self._head = newNode
        self._size += 1
    
    '''Search for a value in the list, return it if found, None otherwise'''
    def find(self, value):
        currentNode = self.SListNode()
        currentNode.next = self._head
        while True:
            if currentNode.next:
                if currentNode.next.value == value:
                    return currentNode.next
                else:
                    currentNode.next = currentNode.next.next
            else:
                return None
                

    '''Remove the first occurance of value.'''
    def remove(self, value):
        currentNode = self.SListNode()
        currentNode.next = self._head
        while True:
            if currentNode.next:
                if value == currentNode.next.value:
                    currentNode.next = currentNode.next.next
                    self._size -= 1
                    return True
                else:
                    if currentNode.next != None:
                        currentNode = currentNode.next
                    else:
                        return False
            else:
                return False

    '''Remove all instances of value'''
    def remove_all(self, value):
        currentNode = self.SListNode()
        currentNode.next = self._head
        while True:
            if currentNode.next:
                if value == currentNode.next.value:
                    currentNode.next = currentNode.next.next
                    self._size -= 1
                else:
                    currentNode = currentNode.next
            else:
                break
            
    '''Convert the list to a string and return it'''
    def __str__(self):
        currentNode = self.SListNode()
        currentNode.next = self._head
        contentString = "["
        if self._head != None:
            for i in range(self._size):
                if currentNode.next:
                    contentString += str(currentNode.next.value)
                    if currentNode.next.next != None:
                        contentString += ', '
                    currentNode = currentNode.next
        contentString += "]"
        return contentString

    '''Return an iterator for the list'''
    def __iter__(self):
        self._iterator = 0
        return self

    def __next__(self):
        if self._iterator < self._size:
            nextIteration = self._iterator
            self._iterator += 1
            return nextIteration
        else:
            raise StopIteration

    '''Return the item at the given index, or throw an exception if invalid index'''
    def __getitem__(self, index):
        currentNode = self.SListNode()
        currentNode.next = self._head
        if index >= self._size:
            raise ValueError("Chosen index is too large")
        elif index < 0:
            raise ValueError("Chosen index is negative")
        else:
            for i in range(index - 1):
                currentNode = currentNode.next
            if currentNode:
                return currentNode.value

    def size(self):
        return self._size
    
