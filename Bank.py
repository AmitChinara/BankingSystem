import random


class Bank:

    def __init__(self):
        self.customer_info_filename = None

    def loadData(self):
        pass

    # Generates a six-digit account number.
    def generateAccountNumber(self):
        return str(random.randint(100000, 999999))
