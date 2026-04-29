## for queue rear means insertion and front means deletion.

class Queue:
    def __init__(self):
        self.front=-1
        self.rear=-1
        self.que=[0]*8

    def enqueue(self,e):
        if self.rear==7:
            print("Queue Overflow")
        else:
               if self.front==-1:
                   self.front=0
               self.rear+=1 
               self.que[self.rear]=e
               print("Insertion of Queue", e)

    def dequeue(self,e):
        if self.front==-1:
            print("Queue Underflow")
        else:
            e=self.que[self.front]
            self.front+=1
            print("Deletion of Queue", e)
            return e

    def display(self):
        if self.front==-1:
            print("Empty")
        else:
            for i in range(self.front, self.rear+1):
                print(self.que[i])

s=Queue()
s.enqueue(10)
s.enqueue(20)
s.dequeue(20)
s.enqueue(30)
s.enqueue(50)
s.dequeue(20)
s.dequeue(10)
s.display()
