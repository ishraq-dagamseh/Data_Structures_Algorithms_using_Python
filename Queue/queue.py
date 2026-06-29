class Queue1:
    def __init__(self):
        self.q=[]

    def enqueue(self, value):
        self.q.append(value)


    def dequeue(self):
        self.q.pop(0)

    def front(self):
        return self.q[0]


queu1=Queue1()
queu1.enqueue(4)
queu1.enqueue(8)
queu1.enqueue(7)

print(queu1.front())
queu1.dequeue()
print(queu1.front())


      
