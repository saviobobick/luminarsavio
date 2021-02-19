import datetime
class bank:
    bname="State Bank"
    def create_acc(self,acno,name,phno,bal):
        self.acno=acno
        self.name=name
        self.phno=phno
        self.bal=bal
    def deposit(self,amount):
        self.bal+=amount
        print("Your",bank.bname,"account is credited with",amount,"on",datetime.datetime.now(),"Your available balance is",self.bal)
    def withdraw(self,amount):
        if amount>self.bal:
            print("Insufficient balance")
        else:
            self.bal-=amount
            print("Your",bank.bname,"account is debited with", amount,"on",datetime.datetime.now(),"Your available balance is", self.bal)
    def balance(self):
        print("Your available balance is",self.bal)
obj=bank()
obj.create_acc(101,"Savio Deepak",983387783,15000)
obj.deposit(1000,)
obj.withdraw(150)
obj.balance()