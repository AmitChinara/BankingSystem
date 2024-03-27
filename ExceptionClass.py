class InvalidChoiceException(Exception):
    def __init__(self, choice):
        super().__init__(f'"{choice}" is an invalid choice.')


class NoAvailableAccountNumberException(Exception):
    def __init__(self):
        super().__init__(f'All the random numbers has been generated. Kindly contact the manager: Mr. Amit Chinara')


class AccountNumberNotFoundException(Exception):
    def __init__(self, account_number):
        super().__init__(f'The account number: {account_number} is not available in the database.')


class InvalidAmountException(Exception):
    def __init__(self, amount):
        super().__init__(f'Amount: {amount} is invalid.')


class InsufficientBalanceException(Exception):
    def __init__(self, amount):
        super().__init__(f'Amount: {amount:.2f} is insufficient.')