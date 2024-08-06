class Queue:

    def __init__(self,max_size):
        self.__max_size = max_size
        self.__queue = [None]*max_size
        self.__front = max_size+1
        self.__rear = -1

    def isEmpty(self):
        if (self.__front == self.__rear):
            return True
        else:
            return False

    def isFull(self):
        if(self.__front == self.__max_size):
            return True
        return False

    def enqueue(self,data):
        if self.isFull():
            print("Queue is Full")
        else:
            self.__rear += 1
            self.__queue[self.__rear] = data

    def dequeue(self):
        if self.isEmpty():
            print("The Queue is Empty")
        else:
            self.__rear -= 1
            self.__queue.pop(0)

    def display(self):
        for i in self.__queue:
            print(i)
    
# q = Queue(4)

# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)

# q.display()

# q.dequeue()
# q.display()

max_size = int(input("Enter the size of Queue: "))
q = Queue(max_size)

ch = input("\nContinue(1(Yes)/0(No)): ")
while ch == '1':

    print("\nSelect amongst the following: ")
    print("1) Enqueue Data")
    print("2) Dequeue Data")
    print("3) Display Queue")  
    print("4) Exit")  
    option = int(input("Enter your option: "))

    if option == 1:
        q.enqueue(int(input("Enter a Number: ")))
    elif option == 2:
        q.dequeue()
    elif option == 3:
        q.display()
    elif option == 4:
        exit()
    else:
        print("Invalid Option")

    ch = input("\nContinue(1(Yes)/0(No)): ")