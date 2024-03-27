class Helper:

    def __init__(self):
        pass

    def displayMenu(self):
        print("++---------------|| WELCOME TO SONAL BANK ||-------------------++\n"
              "||                   1. Account Creation                       ||\n"
              "||                   2. Deposit                                ||\n"
              "||                   3. Withdrawal                             ||\n"
              "||                   4. Balance Inquiry                        ||\n"
              "||                   5. Close Account                          ||\n"
              "||                   6. Exit Application                       ||\n"
              "++-------------------------------------------------------------++\n")

    def displayDetails(self, account_number, name, balance):
        print("+=================================================+\n"
              f"  Account Number: {account_number}\n"
              f"  Account Holder Name: {name}\n"
              f"  Available Balance: ${balance:.2f}\n"
              "+=================================================+\n")
