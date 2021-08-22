def show_balance(balance):
    # assume that balance is passed from parameter balance and will be a float value
    balance = float(balance)
    return balance


def deposit(balance):
    # takes in input for deposit amount
    deposit_amount = float(input("Enter amount to deposit : $"))
    balance = float(balance)
    return balance + deposit_amount


def withdraw(balance): #takes input for withdraw amount
    withdraw_amount = float(input("Enter the amount to withdraw: $"))
    balance = float(balance)
    return balance - withdraw_amount


def logout(name): #says goodbye and logs out
    return "Goodbye " + name
