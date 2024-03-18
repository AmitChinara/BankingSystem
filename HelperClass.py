class Helper:

    def __init__(self):
        pass

    def displayMenu(self):
        print("++---------------|| WELCOME TO SONAL BANK ||-------------------++")
        print("||                   1. Account Creation                       ||")
        print("||                   2. Deposit                                ||")
        print("||                   3. Withdrawal                             ||")
        print("||                   4. Balance Inquiry                        ||")
        print("||                   5. Close Account                          ||")
        print("||                   6. Exit Application                       ||")
        print("++-------------------------------------------------------------++")

    def displayDetails(self, account_number, name, balance):
        print("+=================================================+")
        print(f"  Account Number: {account_number}")
        print(f"  Account Holder Name: {name}")
        print(f"  Available Balance: ${balance:.2f}")
        print("+=================================================+")
