import sys

balance = 6000
choice = 0
transactions = []
attempt = 0

print("========================")
print("     ATM SYSTEM            ")
print("========================")

pin_verified = False

while attempt < 3:
    pin = int(input("Enter your pin: "))
    attempt += 1
    if pin == 1432:
        pin_verified = True
        break
    else:
        print("enter valid pin")

if not pin_verified:
    print("Too many incorrect attempts. Card blocked.")
    sys.exit()

while choice != 4:
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        transactions+=1
        print("Your balance is ", balance)

    elif choice == 2:
        deposit = int(input("enter the amount you want to deposit: "))
        if deposit <= 0:
            print("enter valid amount")
        else:
            print("Your deposit is ", deposit)
            balance += deposit
            transactions += 1
            print("Your balance is ", balance)

    elif choice == 3:
        withdraw = int(input("enter the amount you want to withdraw: "))
        if withdraw <= 0:
            print("enter valid amount")
        elif withdraw <= balance:
            print("Your withdraw is ", withdraw)
            balance -= withdraw
            transactions += 1
            print("Your balance is ", balance)
        else:
            print("insufficient funds")

    elif choice == 4:
        print("exit")
        print("total transactions: ", transactions)
        print("Thank you for using this ATM. Visit Again")
        sys.exit()
