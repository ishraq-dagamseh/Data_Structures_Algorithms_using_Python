class Stack:
    def __init__(self):
        self.s=[]#create stack
    #insert element
    def push(self, value):
        self.s.append(value)

    #isEmpty
    def isEmpty(self):
        if len(self.s)==0:
            return True
        else:
            return False
        
    #remove last element
    def pop(self):
        if self.isEmpty():
            print("Error")
        else:
            self.s.pop()  

    #define top
    def top(self):
        if self.isEmpty():
            print("Error")
            return None
        else:
           return self.s[-1]


stack1=Stack()
stack1.push(6)
print(stack1.top())
stack1.push(7)
stack1.push(9)
stack1.pop()                      
print(stack1.top())
