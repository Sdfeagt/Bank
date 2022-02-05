from personal_account import PersonalAccount
from savings_account import SavingsAccount


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.accounts = []

    def get_name(self):
        return self.name

    def get_customers(self):
        return self.customers

    def get_customers_by_name(self, name):
        filtered = []
        if len(self.customers) != 0:
            i = 0

            while i < len(self.customers):
                if self.customers[i].get_name() == name:
                    filtered.append(self.customers[i])
                i += 1
            return filtered
        return filtered

    def get_customer_by_id(self, idnew):
        filtered = []
        if len(self.customers) > 0:
            i = 0
            while i < len(self.customers):
                if self.customers[i].get_id() == idnew:
                    filtered.append(self.customers[i])
                i += 1
            return filtered
        return None

    def add_savings_account(self, customer):
        if customer in self.customers:
            new_account = SavingsAccount(customer)
            self.accounts.append(new_account)
            return new_account
        else:
            return None

    def add_personal_account(self, customer):
        if customer in self.customers:
            new_account = PersonalAccount(customer)
            print("Added a new personal account")
            self.accounts.append(new_account)
            print("New list of accounts:", self.accounts)
            return new_account
        else:
            return None

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def remove_customer(self, customer):
        if customer in self.customers:
            self.customers.remove(customer)

    def get_accounts(self, customer):
        i = 0
        filtered = []
        while i < len(self.accounts):
            if self.accounts[i].owner_name() == customer.get_name():
                filtered.append(self.accounts[i])
            i += 1
        return filtered
