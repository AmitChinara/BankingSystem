class InvalidChoiceException(Exception):
    def __init__(self, choice):
        super().__init__(f'"{choice}" is a invalid choice.')