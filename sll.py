# Course: CS261 - Data Structures
# Student Name: Ryan Farol
# Assignment: Assignment 3 SLL
# Description: The Singly Linked Class as multiple functions below: add front, add back, insert at index, remove front
# remove back, remove at index, get front, get back, remove, count, and slice. Each function uses the SLNode class.



class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """add_front function checks if the list is empty. If empty, adds the node between the head and tail. If not,
        adds it to the front of the list/"""
        if self.head.next == self.tail: # checks if list is empty
            self.head.next = SLNode(value) # adds node to the list
            self.head.next.next = self.tail # moves tail to the end
            return
        else:
            temp = self.head.next # initialize current head of list
            self.head.next = SLNode(value) # add in the new node
            self.head.next.next = temp # move current head of list over one
            return

    def add_back(self, value: object) -> None:
        if self.head.next == self.tail:  # checks if we are at the back of the list
            self.head.next = SLNode(value)  # adds node to the list
            self.head.next.next = self.tail  # moves tail to the end
            return
        else:
            pointer = self.head.next # initialize the pointer to the first index of the list
            for i in range(self.length()): # traverse the list to find last node
                if pointer.next == self.tail: # checks to see once the end of list is met
                    pointer.next = SLNode(value) # adds node to the end of the list
                    pointer.next.next = self.tail # moves tail to the end
                pointer = pointer.next # move over other nodes
            return
        pass

    def insert_at_index(self, index: int, value: object) -> None:
        """insert_at_index function takes the index and value and adds it into the linked list. First, it checks if the
        index is applicable. If not, raises exception. Then it checks if the list is empty or at the beginning of the list,
        and adds it in. If not, list is """
        if index < 0 or index > self.length(): # checks if index is 0 or if index is larger than the length of the list.
            raise SLLException
        elif self.head.next == self.tail: # checks if list is empty and adds the add
            self.head.next = SLNode(value)
            self.head.next.next = self.tail
            return
        elif index == 0: # checks if index is at 0
            temp = self.head.next # intialize the first node of the list
            self.head.next = SLNode(value) # add in new node
            self.head.next.next = temp # move first node ot the right
            return
        else:
            curr_pointer = self.head.next # set a pointer to the first node of the list
            prev_pointer = self.head # set a pointer to the sentinel (true beginning of list)
            counter = 0 # initialize counter
            # We set a counter to make sure we go through the list and keeping track of the previous and current
            # pointer. A for loop wouldn't work since it only keeps track of the current pointer which would make us
            # lose the previous part of the list.
            while counter != index:
                prev_pointer = curr_pointer
                curr_pointer = curr_pointer.next
                counter += 1
            prev_pointer.next = SLNode(value) # once index is met, add in the value to current pointer
            prev_pointer.next.next = curr_pointer # put the first saved pointer and move it to the right
            return
        pass

    def remove_front(self) -> None:
        """remove_front function first checks if the list is empty. If not empty, the function removes the first node
        in the front"""
        if self.is_empty() == True: # checks if list is empty
            raise SLLException # raises exception if true
        else:
            current_head = self.head.next.next # initialize the new head
            self.head.next = current_head # moves over current head to the new head
            return
        pass

    def remove_back(self) -> None:
        """remove_back function first checks if the list is empty. If empty, exception is raised. If the list only
        consists of one node, it removes it. If not, the list is traversed to the find the last node. Once at the end,
        the last node is removed and the tail is put at the end."""
        if self.is_empty() == True:  # checks if list is empty
            raise SLLException  # raises exception if true
        if self.length() == 1: # if there is only one node in the list, node is removed
            current_head = self.head.next.next # initialize the new head
            self.head.next = current_head # moves over current head to the new head
            return
        else:
            pointer = self.head.next  # initialize the pointer to the first index of the list
            end = 0 # initialize a variable to use for the end of the list
            for i in range(self.length()):  # traverse the list to find last node
                if pointer.next == self.tail: # checks to see once the end of list is met
                    end.next = pointer.next # store tail of list into end.next variable
                end = pointer # last node is removed and new end is established
                pointer = end.next  # tail is now moved to the end
            return
        pass

    def remove_at_index(self, index: int) -> None:
        """remove_at_index function first checks if the index is less than 0 or if the index is larger than the length.
        If they are, it raises the index. Then it checks if the index is at 0 which removes the node from the front
        of the list. If not, the list is traversed to reach the end. It checks if the end of the list is the tail and
        raises the exception if met. If not, the node is removed at the index placed"""
        if index < 0 or index > self.length():  # checks if index is 0 or if index is larger than the length of the list.
            raise SLLException
        if index == 0:
            current_head = self.head.next.next  # initialize the new head
            self.head.next = current_head  # moves over current head to the new head
            return
        else:
            curr_pointer = self.head.next # set a pointer to the first node of the list
            prev_pointer = self.head # set a pointer to the head sentinel (true beginning of list)
            for end in range(index): # traverse through linked list using the index as the end point.
                prev_pointer = curr_pointer
                curr_pointer = curr_pointer.next
            if curr_pointer == self.tail: # this checks if the end of the index is the tail, raises exception if met
                    raise SLLException
            else:
                prev_pointer.next = curr_pointer.next # if not, remove the node at index
                return
        pass

    def get_front(self) -> object:
        """get_front function first checks if the list is empty. If empty, exception is raised. If not, return the value
        of the first node"""
        if self.is_empty() == True:
            raise SLLException
        else:
            return self.head.next.value
        pass

    def get_back(self) -> object:
        """get_back function gets the last node within the list"""
        if self.is_empty() == True: # checks if list is empty, and if empty, raises exception
            raise SLLException
        pointer = self.head.next # initialize pointer to the first node
        for nodes in range(self.length()-1): # traverse through the list
            pointer = pointer.next # move the pointer to the last node of the list
        return pointer.value # return value
        pass

    def remove(self, value: object) -> bool:
        """remove function takes the value and searches through the list to check if the value exists. If it does,
        the value is removed."""
        if self.is_empty() == True: # checks if list is empty. If empty, returns False
            return False
        elif self.head.next.value == value: # if the first value matches the value inputted, it removes the first node
            self.head = self.head.next
            return True
        else:
            curr_pointer = self.head.next # initialize current position
            prev_pointer = 0 # intialize a previous position variable
            # while the current position does not equal the value, it moves throughout the list
            while curr_pointer != None and curr_pointer.value != value:
                prev_pointer = curr_pointer
                curr_pointer = curr_pointer.next
            if curr_pointer != None: # once found, the node is removed
                prev_pointer.next = curr_pointer.next
                return True
            return False
        pass

    def count(self, value: object) -> int:
        """count function first checks if list is empty and returns 0 if empty. Then it sets a count variable and
        traverses through the list. If the pointer equals the value entered, iterate the count. Once it traverses
        through the entire list, the count is returned."""
        if self.is_empty() == True: # checks if list is empty and returns 0 if true
            return 0
        else:
            pointer = self.head.next # set pointer to first node
            count = 0 # intialize count variable
            for i in range(self.length()): # traverse through the list
                if pointer.value == value: # checks if pointer value equals the value entered
                    count += 1 # if equal, iterate the count variable
                pointer = pointer.next # move through the list
            return count
        pass

    def slice(self, start_index: int, size: int) -> object:
        """slice function creates a new linkedlist object and takes a start index and size variable. The new object
        will have the head node of the start index from the original linked list. The size of the list is determined
        by the size entered."""
        if self.is_empty() == True or size < 0 or start_index < 0 or size > self.length() or start_index == self.length() \
            or size + start_index > self.length():
            # checks if the list is empty, size and start index are not negative, size is smaller than the length,
            # start index is not at the end of the list, and the start index and size stay within the bounds of the
            # length. Raises execption if one is met.
            raise SLLException
        sliced_list = LinkedList() # create new list
        pointer = self.head.next # initialize first node for new list
        for new_node in range(start_index): # iterate throughout the original list using the start index
            pointer = pointer.next # store within the new variable
        for new_size in range(size): # iterate through the new list by using the size entered
            sliced_list.add_back(pointer.value) # add the values one by one using the add back function
            pointer = pointer.next # keep adding until the list is filled
        return sliced_list
        pass


if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    list = LinkedList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)


    print('\n# add_back example 1')
    list = LinkedList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)


    print('\n# insert_at_index example 1')
    list = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))

    print('\n# remove_front example 1')
    list = LinkedList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))


    print('\n# remove_back example 1')
    list = LinkedList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)


    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)


    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))


    print('\n# get_back example 1')
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())


    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)


    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))


    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")


    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")