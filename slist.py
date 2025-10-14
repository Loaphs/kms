
class SList:
    class SListNode:
        def __init__ (self, value = None):
            self.value = value
            self.next = None

    def __init__ (self):
        self._head = None
        self._size = 0
        self._iterator = 0
        self._currentNode = self.SListNode()

    '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
    def insert(self, value):
        newNode = self.SListNode(value)
        if self._head != None:
            self._currentNode.next = self._head
            for i in range(self._size):
                if self._currentNode.next == None:
                    print("push back")
                    self._currentNode.next = newNode
                    break
                else:
                    print("hi")
                    if value > self._currentNode.next.value:
                        print("iterating")
                        self._currentNode.next = self._currentNode.next
                        print(self._currentNode)
                        print(self._currentNode.next)
                    else:
                        print("inserted")
                        newNode.next = self._currentNode.next
                        self._currentNode.next = newNode
        else:
            self._head = newNode
        self._size += 1
    
    '''Search for a value in the list, return it if found, None otherwise'''
    def find(self, value):
        self._currentNode.next = self._head
        while True:
            if self._currentNode.next.value == value:
                return self._currentNode.next
            else:
                return None

    '''Remove the first occurance of value.'''
    def remove(self, value):
        self._currentNode.next = self._head
        while True:
            if value == self._currentNode.next.value:
                self._currentNode.next = self._currentNode.next.next
                self._size -= 1
                return True
            else:
                if self._currentNode.next != None:
                    self._currentNode = self._currentNode.next
                else:
                    return False

    '''Remove all instances of value'''
    def remove_all(self, value):
        self._currentNode.next = self._head
        while True:
            if value == self._currentNode.next.value:
                self._currentNode.next = self._currentNode.next.next
                self._size -= 1
            else:
                if self._currentNode.next != None:
                    self._currentNode = self._currentNode.next
                else:
                    break

    '''Convert the list to a string and return it'''
    def __str__(self):
        self._currentNode.next = self._head
        contentString = "["
        if self._head != None:
            for i in range(self._size):
                contentString += str(self._currentNode.next.value)
                if self._currentNode.next != None:
                    contentString += ', '
                print("moving node")
                print(self._currentNode.value)
                print(self._currentNode.next.value)
                self._currentNode = self._currentNode.next
        contentString += "]"
        return contentString

    '''Return an iterator for the list'''
    def __iter__(self):
        self._iterator = 0
        return self

    def __next__(self):
        nextIteration = self._iterator
        self._iterator += 1
        return nextIteration

    '''Return the item at the given index, or throw an exception if invalid index'''
    def __getitem__(self, index):
        self._currentNode.next = self._head
        for i in range(index - 1):
            self._currentNode = self._currentNode.next
        return self._currentNode.next

    def size(self):
        return self._size
    
