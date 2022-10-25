class BankAccount:

    def __init__(self):
        print(f"constructor from BankAccount {self}")

    def __del__(self):
        print(f"destructor from BankAccount {self}")


account1 = BankAccount()
print(account1)

account2 = BankAccount()
print(account2)

# print(account2 == account1)
# print(account3 == account2)
