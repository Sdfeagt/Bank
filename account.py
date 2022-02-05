class Account:
    def __init__(self, customer):
        self.customer = customer
        self.balance = 0

    def get_customer(self):
        return self.customer

    def get_balance(self):
        return self.balance

    def deposit(self, sum):
        self.balance += sum

    def withdraw(self, sum):
        if sum <= self.balance:
            self.balance = self.balance - sum
            return True
        else:
            return False

    def transfer_to(self, account, sum):
        return False

    def owner_name(self):
        customerX = self.get_customer()
        return customerX.get_name()
