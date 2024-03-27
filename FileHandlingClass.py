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

    def writeData(self, bank_obj):
        data = bank_obj.data
        content = ""

        for account_number in data:
            details = data[account_number]
            content += f'{account_number}:{details[0]}:{details[1]}\n'

        if os.path.exists(self.customer_info_filename):
            with open(self.customer_info_filename, "w") as file:
                 file.write(content)
                 file.close()
