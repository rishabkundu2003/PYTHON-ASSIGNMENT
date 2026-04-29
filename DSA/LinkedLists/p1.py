class node:
    def __init__(self,item):
        self.info=item
        self.next=None
class sLinkedList:
    def __init__(self):
        self.start=None
    def insert1(self,item):
        nd=node(item)
        if self.start==None:
            self.start=nd
            return
        temp=self.start
        while temp.next!=None:
            temp=temp.next
        temp.next=nd
    def insert2(self,item):
        nd=node(item)
        nd.next=self.start
        self.start=nd
    def delete1(self):
        if self.start==None:
            print("Empty")
            return
        self.start=self.start.next
    def delete2(self):
        if self.start==None:
            print("Empty")
            return
        if self.start.next==None:
            self.start=None
            return
        temp=self.start
        while temp.next:
            temp=temp.next
        temp.next=None
    def display(self):
        temp=self.start
        while temp!=None:
            print(temp.info)
            temp=temp.next
l=sLinkedList()
l.insert1(10)
l.insert1(20)
l.insert2(30)
l.insert2(40)
l.display()
l.delete1()
l.display()
l.delete2()
l.display()
