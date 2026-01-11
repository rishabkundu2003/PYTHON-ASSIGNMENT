class student:
    def __init__(self):
        self.marks=[]
    def getmarks(self):
        try:
            for i in range(1,5):
                m=int(input("Enter the marks"))
                if m<0 or m>100:
                    raise ValueError("Marks is not valid")
                self.marks.append(m)
        except ValueError as e:
            print("Error",e)
            self.marks=[]
    def average(self):
        if len(self.marks)==4:
            a=sum(self.marks)//4
            print("Average",a)
        else:
            print("Invalid")
obj=student()
obj.getmarks()
obj.average()
