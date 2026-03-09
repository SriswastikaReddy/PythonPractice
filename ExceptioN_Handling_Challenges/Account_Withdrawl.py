class InsufficientFundsError(Exception):
    pass

def withdraw(balance,amount):
    if (amount > balance):
        raise InsufficientFundsError("You don't have enough money!")
    else:
        balance -= amount
        return balance

balance = 100
amount = int(input("How much money do you want to withdraw? "))
try:
    balance = withdraw(balance,amount)
    print("account balance left",balance)
    print("Thank you for withdrawing!")
except InsufficientFundsError as e:
    print(e)
    