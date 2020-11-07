# Course: CS261 - Data Structures
# Student Name: Ryan Farol
# Assignment: Assignment 3 - Queue from Stacks
# Description: The Queue class has 2 methods: enqueue and dequeue which use the max_stack class.


from max_stack_sll import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new Queue based on two stacks
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.s1 = MaxStack()  # use as main storage
        self.s2 = MaxStack()  # use as temp storage

    def __str__(self) -> str:
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.s1.size()) + " elements. "
        out += str(self.s1)
        return out

    def is_empty(self) -> bool:
        """
        Return True if queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.size()

    # ------------------------------------------------------------------ #

    def enqueue(self, value: object) -> None:
        """enqueue function adds the values to end of the list"""
        return self.s1.push(value)
        pass

    def dequeue(self) -> object:
        """dequeue function removes the first element of the que and returns it. If the stack is empty, it raises Queue
        Exception"""
        if self.s1.is_empty()== True: # if size of array is 0, raise exception
            raise QueueException
        else:
            first_que = self.s1.top() # initialize the first value of the que
            self.s1.pop() # remove it
        return first_que # return variable
        pass

# BASIC TESTING
if __name__ == "__main__":
    pass

    print('\n# enqueue example 1')
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
        print(q)

    print('\n# dequeue example 1')
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
        print(q)
        for i in range(6):
            try:
                print(q.dequeue(), q)
            except Exception as e:
                print("No elements in queue", type(e))