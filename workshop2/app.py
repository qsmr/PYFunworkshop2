from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

#TASK2
print(" ===Automated Teller Machine=== ")
#name = ""
name = input("Enter name to register: ") #I changed this variable name from user to name because it seemed like the directions kept referring to this variable as "name" and not "user" 
pin = input("Enter PIN: ")
balance = "0"
print(name + " has been registered with a starting balance of $" + balance)
print()

#TASK3 - 1st while loop
#print(" ===Automated Teller Machine=== ")
#print("LOGIN")
#name_to_validate = input("Enter Name: ")
#pin_to_validate = input("Enter PIN: ")

#change the above to a function   -  nope the original works just fine..LOL
# def login_screen(name_to_validate, pin_to_validate):
    #print(" ===Automated Teller Machine=== ")
    #print("LOGIN")
    #name_to_validate = input("Enter Name: ")
    #pin_to_validate = input("Enter PIN: ") 

#while name_to_validate != name and pin_to_validate != pin:
while True:
    print(" ===Automated Teller Machine=== ")
    print("LOGIN")
    name_to_validate = input("Enter Name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login Successful!")
        break
    else:
        print("Invalid Credentials!")
    

#TASK3 4 5 second while loop
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        print("Current Balance: $", account.show_balance(balance))
    elif option == "2":
        print("Current Balance: $", account.deposit(balance))
    elif option == "3":
        print("Current Balance: $", account.withdraw(balance))
    elif option =="4":
        print(account.logout(name))
        break 



