from account import Account


class PersonalAccount(Account):
    def __init__(self, customer):
        super().__init__(customer)
        self.balance = 0

    def transfer_to(self, account, sum):
        if self.balance > 0:
            if self.balance - sum >= 0:
                self.balance -= sum
                account.balance += sum
                return True
        return False
