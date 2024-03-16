import random


class Bank:

    def __init__(self):
        pass

    # Generates a six-digit account number for a new bank account.
    def generateAccountNumber(self):
        return str(random.randint(100000, 999999))
