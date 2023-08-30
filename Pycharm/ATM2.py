class bank():
    def __init__(self,balance,withdraw):
        self.bal = balance
        self.witt= withdraw
    def bamount(self):
        print("Account Balance :",self.bal)
    def wamount(self):
        self.witt = int(input("Enter the amount to withdraw :"))
    def remaining(self):
        print("Remaining Balance :",self.bal-self.witt)

pin =int(input("Enter your pin"))

if pin<999:
    print("Invalid pin")
else:
    ban = bank(20000,0)
    ban.bamount()
    ban.wamount()
    ban.remaining()