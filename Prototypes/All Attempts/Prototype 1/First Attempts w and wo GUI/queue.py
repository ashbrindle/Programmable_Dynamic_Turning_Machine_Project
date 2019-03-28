
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.back = None
        self.count = 0

    def enqueue(self, value):
        if self.front == None:  #queue empty
            self.front = Node(value)
            self.back = self.front
        else:
            self.back.next = Node(value)
            self.back = self.back.next
        self.count += 1 #size of the queue

    def dequeue(self, value):
        if self.front == None:  #queue empty
            return None
        return_value = self.front.value
        if self.front == self.back:
            self.front = self.back = None
        else:
            self.front = self.front.next
        self.count -= 1
        return return_value

    def __len__(self):
        return self.count