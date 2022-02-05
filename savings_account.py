from account import Account


class SavingsAccount(Account):
    def __init__(self, customer):
        super().__init__(customer)
        self.balance = 0

    def transfer_to(self, account, sum):
        customer_local = self.get_customer()
        customer_foreign = account.get_customer()
        if self.balance > 0:
            if self.balance - sum >= 0:
                if customer_local == customer_foreign:
                    self.balance -= sum
                    account.balance += sum
                    return True
        return False
