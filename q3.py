''''
This program creates a circular queue and adds elements to it as well
as removing them. This program follows the FIFO method and since it is
circular, after the last spot in the array, it will go back to the first

Array Based list Circular Queue Implemented

Student Id: 20232676
'''


class CircularQueue:

    def __init__(self,capacity):

        """
        This function initializes all the variables we will be
        using in our code. The size represents the number of elements
        inside the array. the array is the actal array itself with None
        initialized. The tail and head are also initialized since it will
        be used later to determine the new tail and head spots
        """
        self.array = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = capacity

    def is_full(self):
        """This function determines whether the queue is full"""
        return self.capacity == self.size

    def enqueue(self,element):
        """
        This function adds an element to the back (tail) of the queue.
        If the queue is full, it displays a message informing that the
        queue is full. If not, the element is added to the queue and then
        the tail will point to the next element.
        """
        if(self.is_full()):
           raise Exception("Queue is full")
        else:
            #add the new element to the end (tail)
            self.array[self.tail] = element
            #determine the new location for the tail
            self.tail = (self.tail + 1) % self.capacity
            self.size += 1

        
    def dequeue(self):
        """
        This method checks to see if the queue is empty, if it is, it returns
        nothing and informs us the queue is empty. Otherwise, the first (head)
        element gets removed and returned to the console.
        """

        #the queue is empty
        if(self.size == 0):
            raise Exception("Queue is empty")
            return None
        #save the element that will get removed
        removed_element = self.array[self.head]
        #determine the new location for the head
        self.head = (self.head + 1) % self.capacity
        self.size-=1
        return removed_element

def main():
    """ The main method tests the program by adding different test cases"""
    my_queue=CircularQueue(6)
    my_queue.enqueue(10)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    my_queue.enqueue(5)
    print("The size of the queue is: ")
    print(my_queue.size)
    print("An element is being dequeued: ")
    print(my_queue.dequeue())
    print("The size of the queue is now : ")
    print(my_queue.size)
    my_queue.enqueue(20)
    print("An element has been enqueued")
    print("The size of the queue is now: ")
    print(my_queue.size)
    print("An element is being dequeued: ")
    print(my_queue.dequeue())
    print("The size of the queue is now: ")
    print(my_queue.size)



if __name__ == "__main__":
    main()
        
        





