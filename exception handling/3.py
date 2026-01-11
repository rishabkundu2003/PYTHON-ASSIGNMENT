class autherror:
    def __init__(self):
        self.password=2218
        self.a=0
    def authenticate(self):
        try:
            p=int(input("Enter a no"))
            if p==self.password:
                print("Login")
                print(f"Attempts:{self.a}")
            else:
                self.a+=1
                print("Wrong")
                print(f"Attempts:{self.a}")
            if self.a==3:
                print("Disabled")
        except:
            print("Error occurred")
user=autherror()
while user.a<3:
    user.authenticate()
