class Helper:

    def __init__(self):
        pass

    def displayMenu(self):
        print("++---------------|| WELCOME TO SONAL BANK ||-------------------++"
              "||                   1. Account Creation                       ||"
              "||                   2. Deposit                                ||"
              "||                   3. Withdrawal                             ||"
              "||                   4. Balance Inquiry                        ||"
              "||                   5. Close Account                          ||"
              "||                   6. Exit Application                       ||"
              "++-------------------------------------------------------------++")

    def displayDetails(self, account_number, name, balance):
        print("+=================================================+"
              f"  Account Number: {account_number}"
              f"  Account Holder Name: {name}"
              f"  Available Balance: ${balance:.2f}"
              "+=================================================+")
