class atm():

    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.balance = 0

    def BalanceEnquiry(self):
        print(f"Your have {self.balance} in you account")
        self._greet()

    def Deposit(self, amt):
        if self._check_type(amt):
            self.balance += amt
            print(f"{amt} has been succesfully deposited to your account")
            self.BalanceEnquiry()
        else:
            print(f"Entered amount {amt} is not a valid number")

    def CashWithdrawl(self, amt):
        if self._check_type(amt):
            if self.balance > amt:
                self.balance -= amt
                print(f"{amt} has been sucessfully withdrawn from you account")
                self.BalanceEnquiry()
            else:
                print(f"You don't have sufficint balance")
                self.BalanceEnquiry()
        else:
            print(f"Entered amount {amt} is not a valid number")

    def _greet(self):
        print("Thank you, Have a nice day")

    def _check_type(self, param):
        if type(param) != int:
            return False
        else:
            return True


