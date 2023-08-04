class BankAccount:
    def __init__(self, balance = 0):
        self._balance = balance

    # this is the getter: with property decorator. Normally, balance attribute would be editable from outside as well using obj.balance = 50
    # but using this balance method, we always access balance variable via function call.
    # Hence, it is read only from outside.
    # If we want to edit this var, we should do function call - update_balance
    @property
    def balance(self):
        return self._balance
    def update_balance(self, value):
        self._balance += value


obj = BankAccount(100)
print(obj.balance)
# obj.balance = 200
# print(obj.balance)
obj.update_balance(100)
print(obj.balance)
