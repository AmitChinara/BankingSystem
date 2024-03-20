import os


class FileHandle:

    def __init__(self):
        self.customer_info_filename = 'Data/customer.txt'
        self.data = {}

    def __loadData(self):
        if os.path.exists(self.customer_info_filename):
            with open(self.customer_info_filename, "r") as file:
                content = file.readlines()
                for value in content:
                    account_number, name, balance = value.split(':')
                    self.data[int(account_number)] = [name, float(balance)]

    def getData(self):
        self.__loadData()
        return self.data
