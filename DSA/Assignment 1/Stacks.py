class Stack:
    def __init__(self):
        self.top=-1
        self.stk=[0]*8

    def push(self,e):
        if self.top==7:
            print("Stack Overflow")
        else:
            self.top+=1
            self.stk[self.top]=e
            print("Pushed into stack",e)

    def pop(self,e):
        if self.top==-1:
            print("Stack Underflow")
        else:
            e=self.stk[self.top]
            self.top-=1
            print("Poped from stack",e)
            return e

    def display(self):
        if self.top==-1:
            print("Empty")
        else:
            for i in range(self.top, -1, -1):
                print(self.stk[i])

s=Stack()
s.push(10)
s.push(20)
s.pop(20)
s.push(30)
s.push(50)
s.pop(20)
s.pop(10)
s.display()
