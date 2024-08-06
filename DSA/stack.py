class Stack:

    def __init__(self,max_size):
        self.__top = -1
        self.__max_size = max_size
        self.__stack = [None]*max_size
        

    def isFull(self):
        if(self.__max_size == self.__top-1):
            return True
        return False
        
    def isEmpty(self):
        if(self.__stack[self.__top] == -1):
            return True
        return False

    def push(self,data):
        if self.isFull():
            return False
        else:
            self.__top += 1
            self.__stack[self.__top] = data

    def delete(self):
        if self.isEmpty():
            return False
        else:
            self.__top -= 1
            self.__stack.pop()

    def peek(self):
        if(self.__top == -1):
            print("Stack Empty")
        else:
            top = self.__stack[self.__top]
            print("Top of Stack---->",top)

    def display(self):
        if self.isEmpty():
            print("The Stack is Empty")
        else:
            top = len(self.__stack)-1
            for i in range(top,-1,-1):
                print(self.__stack[i])


max_size = int(input("Enter the size of stack: "))
s = Stack(max_size)

ch = input("\nContinue(Yes/No): ")
while ch == 'Yes' or ch == 'yes' or ch == 'y' or ch == 'Y':

    print("\nSelect amongst the following: ")
    print("1) Push Data")
    print("2) Pop Data")
    print("3) Peek Top Element")
    print("4) Display Stack")  
    print("5) Exit")  
    option = int(input("Enter your option: "))

    if option == 1:
        s.push(int(input("Enter a Number: ")))
    elif option == 2:
        s.delete()
    elif option == 3:
        s.peek()
    elif option == 4:
        s.display()
    elif option == 5:
        exit()
    else:
        print("Invalid Option")

