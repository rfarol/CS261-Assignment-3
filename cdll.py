# Course: CS261 - Data Structures
# Student Name: Ryan Farol
# Assignment: Assignment 3 CDLL
# Description:


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """add_front function adds the node to the front of the doubly linked list"""
        front_node = DLNode(value) # initialize the front_node
        front_node.prev = self.sentinel # previous points to the sentinel
        front_node.next = self.sentinel.next # new front node points to the next direction previous head of the list
        front_node.next.prev = front_node # prev front node points to the previous direction to the new front node
        self.sentinel.next = front_node # place front node in head of list
        return
        pass

    def add_back(self, value: object) -> None:
        """add_back function adds the node to the back of the dounly linked list"""
        back_node = DLNode(value) # initialize back node
        pointer = self.sentinel.prev # point at the back of the list
        pointer.next = back_node # place back node to the end of the list
        back_node.next = self.sentinel # place the sentinel at the end
        back_node.prev = pointer # prev pointer moves over spot to the left
        self.sentinel.prev = back_node # point sentinel back the new back node
        return
        pass

    def insert_at_index(self, index: int, value: object) -> None:
        """insert at index given within the list"""
        if index > self.length() or index < 0: # checks if the index is bigger than the length of less than 0.
            raise CDLLException # raise exception if met
        if self.is_empty() == True or index == 0: # checks if list is empty or index is at 0, call add front method
            self.add_front(value)
            return
        else:
            new_node = DLNode(value) # new node is initialized
            curr_pointer = self.sentinel # point at the front of the list
            counter = 0
            while counter != index: # iterate until the index is met
                curr_pointer = curr_pointer.next
                counter += 1
            curr_pointer.next.prev = new_node # new node is placed
            new_node.next = curr_pointer.next # node points to the next node
            new_node.prev = curr_pointer # node previously points to old index
            curr_pointer.next = new_node # index points back at new node
            return
        pass

    def remove_front(self) -> None:
        """remove_front function checks if the list is empty. If empty, raises exception. If not, removes the front node"""
        if self.is_empty() == True: # checks if list is empty and raises exception
            raise CDLLException
        head_node = self.sentinel.next # initialize the head node
        head_node.next.prev = self.sentinel # remove the node
        self.sentinel.next = head_node.next # point the sentinel back at the new head node
        return
        pass

    def remove_back(self) -> None:
        """remove_front function checks if the list is empty. If empty, raises exception. If not, removes the back node"""
        if self.is_empty() == True:
            raise CDLLException
        end_node = self.sentinel.prev # initialize the end node
        end_node.prev.next = self.sentinel # remove end node
        self.sentinel.prev = end_node.prev # point sentinel back at the new end node
        return
        pass

    def remove_at_index(self, index: int) -> None:
        """remove at index function checks if the index is less than 0 or bigger than the length of the list. Also
        checks if the index is at 0. If 0, call the remove front method. If not, iterate until the index is met and
        remove the node"""
        if index < 0 or index > self.length():  # checks if index is 0 or if index is larger than the length of the list.
            raise CDLLException
        if index == 0: # if index is 0, remove_front method is called
            return self.remove_front()
        else:
            curr_pointer = self.sentinel.next # set a pointer to the first node of the list
            for end in range(index): # traverse through linked list using the index as the end point.
                curr_pointer = curr_pointer.next
            if curr_pointer.value is None: # this checks if the it reaches the end of the index, raises exception if met
                    raise CDLLException
            else:
                curr_pointer.prev.next = curr_pointer.next # once index is met, remove node. point previous node to current
                curr_pointer.next.prev = curr_pointer.prev # point next node to current.
                return
        pass

    def get_front(self) -> object:
        """get_front functions gets the value of the front node"""
        if self.is_empty() == True:
            raise CDLLException
        return self.sentinel.next.value
        pass

    def get_back(self) -> object:
        """get_back function gets the value of the end node"""
        if self.is_empty() == True:
            raise CDLLException
        return self.sentinel.prev.value
        pass

    def remove(self, value: object) -> bool:
        """remove function takes the value and searches through the list to check if the value exists. If it does,
        the value is removed."""
        if self.is_empty() == True:  # checks if list is empty. If empty, returns False
            return False
        elif self.sentinel.next.value == value:  # if the first value matches the value inputted, it removes the first node
            self.remove_front()
            return True
        else:
            curr_pointer = self.sentinel.next  # initialize current position
            prev_pointer = 0  # initialize a previous position variable
            # while the current position does not equal the value, it moves throughout the list
            while curr_pointer.value != None and curr_pointer.value != value:
                prev_pointer = curr_pointer
                curr_pointer = curr_pointer.next
            if curr_pointer.value != None:  # once found, the node is removed
                curr_pointer.prev.next = curr_pointer.next  # once index is met, remove node. point previous node to current
                curr_pointer.next.prev = curr_pointer.prev  # point next node to current.
                return True
            return False
        pass

    def count(self, value: object) -> int:
        """count function first checks if list is empty and returns 0 if empty. Then it sets a count variable and
           traverses through the list. If the pointer equals the value entered, iterate the count. Once it traverses
           through the entire list, the count is returned."""
        if self.is_empty() == True:  # checks if list is empty and returns 0 if true
            return 0
        else:
            pointer = self.sentinel.next  # set pointer to first node
            count = 0  # intialize count variable
            for i in range(self.length()):  # traverse through the list
                if pointer.value == value:  # checks if pointer value equals the value entered
                    count += 1  # if equal, iterate the count variable
                pointer = pointer.next  # move through the list
            return count
        pass

    def swap_pairs(self, index1: int, index2: int) -> None:
        if index1 < 0 or index2 < 0 or index1 > self.length() - 1 or index2 > self.length() - 1 or self.is_empty() == True:
            raise CDLLException # checks if the indexes are valid

        if index1 == index2: # if indexes are the same, return the same list
            return

        # Checks if both indexes are next to each other. We have to use a special method to move one node at time
        # so the links do not get stuck in an infinite loop. This is the check if the nodes need to move one place to
        # the right
        if index1 + 1 == index2:
            counter_index = 0 # initialize index counter
            current_node = self.sentinel.next # initialize head of the list
            prev_node = self.sentinel # set a previous point
            while counter_index != index1: # iterate until index is met
                current_node = current_node.next
                prev_node = prev_node.next
                counter_index += 1
            holder = current_node.next # Store node
            current_node.next = holder.next # set new link to surrounding nodes
            holder.next = current_node # point link back at the current node
            prev_node.next = holder # swap nodes
            return

        # this checks both indexes are next to each other and if the first index needs to be move to the left
        if index1 - 1 == index2:
            counter_index = 0 # initialize index counter
            current_node = self.sentinel.next # initialize head of the list
            prev_node = self.sentinel
            while counter_index != index2:  # iterate until index is met. NOW USE INDEX 2 instead of index 1
                current_node = current_node.next
                prev_node = prev_node.next
                counter_index += 1
            holder = current_node.next
            current_node.next = holder.next
            holder.next = current_node
            prev_node.next = holder
            return

        # finally, below will set two node pointers for index 1 and index 2. Both were iterate through the list until
        # their indexes are met. The previous and next nodes of the current pointers will be stored and then each pointer
        # will swap nodes and re-establish directions from the nodes next to them.
        else:
            counter_index1 = 0 # set counter index 1
            node1 = self.sentinel.next # set pointer to head of list
            while counter_index1 != index1: # traverse until index is met
                node1 = node1.next
                counter_index1 += 1
            prev_node1 = node1.prev # initialize the previous node on current pointer
            next_node1 = node1.next # initialize the next node on current pointer

            counter_index2 = 0 # set counter 2
            node2 = self.sentinel.next # set pointer to head of list
            while counter_index2 != index2:
                node2 = node2.next
                counter_index2 += 1
            prev_node2 = node2.prev # initialize the previous node on current node 2
            next_node2 = node2.next # initialize the next node on current node 2

            prev_node1.next = node2 # establish link with next node 1 to current node 2
            next_node1.prev = node2 # establish link with previous node 1 to current node 2
            prev_node2.next = node1 # establish link with next node 2 to current node 1
            next_node2.prev = node1 # establish link with previous node 2 to current node 1

            node1.prev = prev_node2 # swap node 1 to node 2
            node1.next = next_node2
            node2.prev = prev_node1 # swap node 2 to node 1
            node2.next = next_node1
            return

    def helper_swap_pairs(self, index1, index2):
        return self.swap_pairs(index1, index2)

    def reverse(self) -> None:
        if self.is_empty() == True or self.length() == 1:
            return
        if self.length() % 2 == 0:
            counter = self.length() / 2
            front_index = 0
            last_index = self.length() - 1
            while counter != 0:
                self.helper_swap_pairs(front_index, last_index)
                last_index = last_index - 1
                front_index = front_index + 1
                counter = counter - 1
            return
        else:
            counter = (self.length() - 1)/2
            front_index = 0
            last_index = self.length() - 1
            while counter != 0:
                self.helper_swap_pairs(front_index, last_index)
                last_index = last_index - 1
                front_index = front_index + 1
                counter = counter - 1
            return
        pass

    def sort(self) -> None:
        """
        TODO: Write this implementation
        """
        pass

    def rotate(self, steps: int) -> None:
        """
        TODO: Write this implementation
        """
        pass

    def remove_duplicates(self) -> None:
        """
        TODO: Write this implementation
        """
        pass

    def odd_even(self) -> None:
        """
        TODO: Write this implementation
        """
        pass


if __name__ == '__main__':
    pass

print('\n# add_front example 1')
lst = CircularList()
print(lst)
lst.add_front('A')
lst.add_front('B')
lst.add_front('C')
print(lst)

print('\n# add_back example 1')
lst = CircularList()
print(lst)
lst.add_back('C')
lst.add_back('B')
lst.add_back('A')
print(lst)

print('\n# insert_at_index example 1')
lst = CircularList()
test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
for index, value in test_cases:
    print('Insert of', value, 'at', index, ': ', end='')
    try:
        lst.insert_at_index(index, value)
        print(lst)
    except Exception as e:
        print(type(e))

print('\n# remove_front example 1')
lst = CircularList([1, 2])
print(lst)
for i in range(3):
    try:
        lst.remove_front()
        print('Successful removal', lst)
    except Exception as e:\
        print(type(e))

print('\n# remove_back example 1')
lst = CircularList()
try:
    lst.remove_back()
except Exception as e:\
    print(type(e))
lst.add_front('Z')
lst.remove_back()
print(lst)
lst.add_front('Y')
lst.add_back('Z')
lst.add_front('X')
print(lst)
lst.remove_back()
print(lst)

print('\n# remove_at_index example 1')
lst = CircularList([1, 2, 3, 4, 5, 6])
print(lst)
for index in [0, 0, 0, 2, 2, -2]:
    print('Removed at index:', index, ': ', end='')
    try:
        lst.remove_at_index(index)
        print(lst)
    except Exception as e:
        print(type(e))
print(lst)

print('\n# get_front example 1')
lst = CircularList(['A', 'B'])
print(lst.get_front())
print(lst.get_front())
lst.remove_front()
print(lst.get_front())
lst.remove_back()
try:
    print(lst.get_front())
except Exception as e:
    print(type(e))

print('\n# get_back example 1')
lst = CircularList([1, 2, 3])
lst.add_back(4)
print(lst.get_back())
lst.remove_back()
print(lst)
print(lst.get_back())

print('\n# remove example 1')
lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
print(lst)
for value in [7, 3, 3, 3, 3]:
    print(lst.remove(value), lst.length(), lst)

print('\n# count example 1')
lst = CircularList([1, 2, 3, 1, 2, 2])
print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

print('\n# swap_pairs example 1')
lst = CircularList([0, 1, 2, 3, 4, 5, 6])
test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5), (4, 2), (3, 3), (1, 2), (2, 1))

for i, j in test_cases:
    print('Swap nodes ', i, j, ' ', end='')
    try:
        lst.swap_pairs(i, j)
        print(lst)
    except Exception as e:
        print(type(e))

print('\n# reverse example 1')
test_cases = (
    [1, 2, 3, 3, 4, 5],
    [1, 2, 3, 4, 5],
    ['A', 'B', 'C', 'D']
)
for case in test_cases:
    lst = CircularList(case)
    lst.reverse()
    print(lst)

print('\n# reverse example 2')
lst = CircularList()
print(lst)
lst.reverse()
print(lst)
lst.add_back(2)
lst.add_back(3)
lst.add_front(1)
lst.reverse()
print(lst)

print('\n# reverse example 3')


class Student:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def __eq__(self, other):
        return self.age == other.age

    def __str__(self):
        return str(self.name) + ' ' + str(self.age)


s1, s2 = Student('John', 20), Student('Andy', 20)
lst = CircularList([s1, s2])
print(lst)
lst.reverse()
print(lst)
print(s1 == s2)

print('\n# reverse example 4')
lst = CircularList([1, 'A'])
lst.reverse()
print(lst)

print('\n# sort example 1')
test_cases = (
    [1, 10, 2, 20, 3, 30, 4, 40, 5],
    ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
    [(1, 1), (20, 1), (1, 20), (2, 20)]
)
for case in test_cases:
    lst = CircularList(case)
    print(lst)
    lst.sort()
    print(lst)

print('\n# rotate example 1')
source = [_ for _ in range(-20, 20, 7)]
for steps in [1, 2, 0, -1, -2, 28, -100]:
    lst = CircularList(source)
    lst.rotate(steps)
    print(lst, steps)

print('\n# rotate example 2')
lst = CircularList([10, 20, 30, 40])
for j in range(-1, 2, 2):
    for _ in range(3):
        lst.rotate(j)
        print(lst)

print('\n# rotate example 3')
lst = CircularList()
lst.rotate(10)
print(lst)

print('\n# remove_duplicates example 1')
test_cases = (
    [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
    [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
    [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],
    list("abccd"),
    list("005BCDDEEFI")
)

for case in test_cases:
    lst = CircularList(case)
    print('INPUT :', lst)
    lst.remove_duplicates()
    print('OUTPUT:', lst)
    #
print('\n# odd_even example 1')
test_cases = (
    [1, 2, 3, 4, 5], list('ABCDE'),
    [], [100], [100, 200], [100, 200, 300],
    [100, 200, 300, 400],
    [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E']
)

for case in test_cases:
    lst = CircularList(case)
    print('INPUT :', lst)
    lst.odd_even()
    print('OUTPUT:', lst)
