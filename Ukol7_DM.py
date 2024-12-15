from logging import raiseExceptions


class Queue:
    def __init__(self, maxsize=10):
        self.head = None
        self.tail = None
        self.maxsize = maxsize
        self.actual_size = 0

    def put(self, data):
        # put data in a queue
        if self.full():
            raise Exceptions("Queue is full")#plná fronta
        new_node=Node(tail)
        if self.tail is None:
            #prázdná fronta -> nový tail a head uzel
            self.head = new_node
        else: #není prázdná
            self.tail.next = new_node #nový uzel na konci
            new_node.prev = self.tail #předhozí uzel je tail
            self.tail = new_node #aktualizace na nový tail (poslení nový uzel)
        self.actual_size += 1 # zvětšení aktuální velikosti fronty

    def get(self):
        # get data from a queue
        if self.empty():
            raise Exception("Queue is empty")
        data = self.head.data
        self.head = self.head.next # head na druhý uzel
        if self.head is None:
            self.tail = None # prazdna fronta -> tail i head is None
        if self.head:
            self.head.prev = None #odstranění odkazu na předchozí uzeů
        self.actual_size -= 1 #snížení velikosti
        return data

    def empty(self):
        # is queue empty?
        return self.actual_size == 0


    def full(self):
        # is queue full?
        return self.actual_size >= self.maxsize


    def size(self):
        # what is the size of a queue?
        return self.actual_size



class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None