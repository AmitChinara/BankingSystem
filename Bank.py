import random
from ConstantsClass import Constants
import ExceptionClass as exp
from HelperClass import Helper
from FileHandlingClass import FileHandle


class Bank:

    def __init__(self):
        self.data = FileHandle().getData()
        self.helper = Helper()

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

    def deposit(self):
        choice = input("Do you want to deposit?? (YES/NO) ").upper()
        if choice == 'YES':
            account_number = int(input("Enter your account number: "))
            if account_number in self.data:
                balance = float(input("Enter the amount to deposit: $"))
                if balance <= 0:
                    raise exp.InvalidAmountException(balance)
                self.data[account_number][1] += balance
                return account_number
            else:
                raise exp.AccountNumberNotFoundException(account_number)
        elif choice == 'NO':
            pass
        else:
            raise exp.InvalidChoiceException(choice)
    def withdrawal(self):
        choice = input("Do you want to withdraw the money?? (YES/NO) ").upper()
        if choice == 'YES':
            account_number = int(input("Enter your account number: "))
            if account_number in self.data:
                balance = float(input("Enter the amount to withdraw: $"))
                if balance <= 0:
                    raise exp.InvalidAmountException(balance)
                elif self.data[account_number][1] < balance:
                    raise exp.InsufficientBalanceException(balance)
                self.data[account_number][1] -= balance
                return self.data[account_number][1]
            else:
                raise exp.AccountNumberNotFoundException(account_number)
        elif choice == 'NO':
            pass
        else:
            raise exp.InvalidChoiceException(choice)

    def closeAccount(self):
        choice = input("Do you want to close the account?? (YES/NO) ").upper()
        if choice == 'YES':
            account_number = int(input("Enter your account number: "))
            if account_number in self.data:
                return self.data.pop(account_number)
            else:
                raise exp.AccountNumberNotFoundException(account_number)
        elif choice == 'NO':
            pass
        else:
            raise exp.InvalidChoiceException(choice)
