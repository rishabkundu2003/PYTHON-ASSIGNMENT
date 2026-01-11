class MCA:
    def __init__(self,category,m,math):
        self.category=category
        self.m=m
        self.math=math
        if category=="general" and m>=50:
                return True
        elif category=="reserved" and m>=45:
                return True
        else:
            return False
        try:
            category=input("Enter the category")
            m=int(input("Enter the marks"))
            math=input("Do u have maths in HS or UG (yes/no)")
            jeca=input("Do u have jeca rank? (yes/no)")
            if jeca=="yes":
                rank=int(input("Enter ur rank"))
            if math=="yes":
                print("you r eligible")
            else:
                print("Not")
        except ValueError:
            print("Invalid details")
obj=MCA()

