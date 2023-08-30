pin = int(input("Enter the Pin"))

class bank():
    def __int__(self,bal,withd):
        self.balance = bal
        self.withdraw = withd
    def Bamount(self):
        print("Account Balance :",self.balance)
    def Wamount(self):
       print(self.withdraw)
    def remaining(self):
        print("Remaining Balance : ",self.balance)


pro = bank()
pro.Bamount()
pro.Wamount()
pro.remaining()

