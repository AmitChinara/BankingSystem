import os.path
import random
from ConstantsClass import Constants
import ExceptionClass as exp
from HelperClass import Helper


class Bank:

    def __init__(self):
        self.customer_info_filename = 'Data/customerinfo.txt'
        self.data = {}
        self.helper = Helper()

    def loadData(self):
        if os.path.exists(self.customer_info_filename):
            with open(self.customer_info_filename, "r") as file:
                content = file.readlines()
                for value in content:
                    account_number, name, balance = value.split(':')
                    self.data[int(account_number)] = [name, float(balance)]

    def accountCreation(self):
        choice = input("Do you want to create the account?? (YES/NO) ").upper()
        if choice == 'YES':
            account_number = self.generateAccountNumber()
            name = input("Enter your name: ").upper()
            balance = float(input("Enter your balance: $"))
            self.data[account_number] = [name, balance]

            return account_number
        elif choice == 'NO':
            print("Your account hasn't been created.")
        else:
            raise exp.InvalidChoiceException(choice)

    # Generates a six-digit account number.
    def generateAccountNumber(self):
        if len(self.data) == Constants.AVAILABLE_ACCOUNT_NUMBER:
            raise exp.NoAvailableAccountNumberException()

        account_number = None
        while account_number is None or account_number in self.data:
            account_number = random.randint(Constants.MIN_ACCOUNT_NUMBER, Constants.MAX_ACCOUNT_NUMBER)
        return account_number

    def balanceInquiry(self):
        account_number = int(input("Enter your account number: "))
        if account_number in self.data:
            data = self.data[account_number]
            name = data[0]
            balance = data[1]
            self.helper.displayDetails(account_number, name, balance)
        else:
            raise exp.AccountNumberNotFoundException(account_number)