class InvalidChoiceException(Exception):
    def __init__(self, choice):
        super().__init__(f'"{choice}" is a invalid choice.')


class NoAvailableAccountNumberException(Exception):
    def __init__(self):
        super().__init__(f'All the random numbers has been generated. Kindly contact the manager: Mr. Amit Chinara')


class AccountNumberNotFoundException(Exception):
    def __init__(self, account_number):
        super().__init__(f'The account number: {account_number} is not available in the database.')
